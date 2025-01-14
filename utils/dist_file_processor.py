import os
import shutil
import configparser
import colorama

colorama.init()


def process_dist_file(source_directory: str, dest_directory: str, source_filename: str, destination_file_name: str,
                      should_copy=True, sensitive=False):
    template_filename = f'.{destination_file_name}.template'
    if sensitive:
        template_filename = '.env.dist.template'

    template_file: str = os.path.join(source_directory, template_filename)
    dest_file: str = os.path.join(dest_directory, destination_file_name)
    skip_all = False

    if not os.path.exists(dest_file):
        print(f'{colorama.Fore.GREEN}Copying {template_file} to {dest_file}{colorama.Style.RESET_ALL}')
        print(f'{colorama.Fore.RED} Re-run this script to be able to set the parameters in {dest_file}'
              f'{colorama.Style.RESET_ALL}')
        if should_copy:
            os.makedirs(dest_directory, exist_ok=True)
            shutil.copy2(template_file, dest_directory)
        copied_template_file = os.path.join(dest_directory, template_filename)
        if sensitive:
            shutil.copy2(template_file, dest_file)
        else:
            os.rename(copied_template_file, dest_file)
    else:
        src_config = configparser.ConfigParser()
        src_config.read(source_filename)
        dest_config = configparser.ConfigParser()
        dest_config.read(dest_file)

        for section in src_config.sections():
            if skip_all:
                break
            print(f'{colorama.Fore.WHITE}Configuring section {colorama.Fore.YELLOW}{section}{colorama.Style.RESET_ALL} '
                  f'{colorama.Fore.WHITE}in {dest_file} {colorama.Style.RESET_ALL}')
            for key in src_config[section]:
                if dest_config.has_option(section, key):
                    print(f'{colorama.Fore.LIGHTCYAN_EX}{key}{colorama.Style.RESET_ALL} '
                          f'{colorama.Fore.GREEN}has already a value in {dest_file} section {section}'
                          f'{colorama.Style.RESET_ALL}'
                          f'{colorama.Fore.RED} ...skipping{colorama.Style.RESET_ALL}')
                    continue
                if not dest_config.has_option(section, key):
                    print(f'{colorama.Fore.YELLOW}Variable '
                          f'{colorama.Fore.LIGHTCYAN_EX}{key}{colorama.Style.RESET_ALL}{colorama.Fore.YELLOW} '
                          f'in section {section} is not set.{colorama.Style.RESET_ALL}')
                    value = input(f'>>> {colorama.Fore.LIGHTBLUE_EX}Please provide a value, '
                                  f'press enter to skip to next value,'
                                  f' or type {colorama.Fore.RED}skip{colorama.Style.RESET_ALL} '
                                  f'{colorama.Fore.LIGHTBLUE_EX}to jump to the next configuration file: '
                                  f'{colorama.Style.RESET_ALL}')
                    if value.strip() == 'skip':
                        skip_all = True
                        break
                    if value is None or value.strip() == '':
                        continue
                    dest_config.set(section, key, value)
        with open(dest_file, 'w') as configfile:
            dest_config.write(configfile)
