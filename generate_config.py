import configparser
import os
import shutil
import colorama

# Specify source directory (where your .dist files are) and destination directory
source_dir = 'features/core_config/.dist'
dest_dir = 'features/core_config'

# Get list of .dist files
dist_files = [f for f in os.listdir(source_dir) if f.endswith('.dist')]
template_files = [f for f in os.listdir(source_dir) if f.endswith('.template')]

# Create destination directory if it doesn't exist
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Loop over each .dist file
for dist_file in dist_files:
    src_file = os.path.join(source_dir, dist_file)
    dest_file_name = os.path.splitext(dist_file)[0] + '.ini'
    template_file = os.path.join(source_dir, '.{}.template'.format(dest_file_name))
    dest_file = os.path.join(dest_dir, dest_file_name)
    skip_all = False

    # If the file doesn't exist in destination directory, copy it
    # from template file
    if not os.path.exists(dest_file):
        print(f'{colorama.Fore.GREEN}Copying {template_file} to {dest_file}{colorama.Style.RESET_ALL}')
        print(f'{colorama.Fore.RED} Re-run this script to be able to set the parameters in {dest_file}'
              f'{colorama.Style.RESET_ALL}')
        shutil.copy2(template_file, dest_file)
    else:
        # If the file does exist, merge variables

        # Parse source config file
        src_config = configparser.ConfigParser()
        src_config.read(src_file)

        # Parse destination config file
        dest_config = configparser.ConfigParser()
        dest_config.read(dest_file)
        # Iterate over each variable in source config file
        for section in src_config.sections():
            if skip_all is True:
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
        # Write updated config to destination file
        with open(dest_file, 'w') as configfile:
            dest_config.write(configfile)
