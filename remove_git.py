# remove_git.py
"""
This script should be used to drop the mage2-behave git repository from the current working directory,
in order to include the project as part of the Magento 2 repository.
"""
import os
import shutil
import colorama

print(f'{colorama.Fore.YELLOW}WARNING:{colorama.Style.RESET_ALL} '
      f'{colorama.Fore.RED}This action will delete the .git directory and cannot be undone.{colorama.Style.RESET_ALL}')


def remove_git_dir():
    git_dir = os.path.join(os.getcwd(), '.git')
    if os.path.exists(git_dir):
        print(f'Removing {git_dir}...')
        shutil.rmtree(git_dir)
        print(f'{colorama.Fore.GREEN}Successfully removed .git directory{colorama.Style.RESET_ALL}')
    else:
        print(f'{colorama.Fore.YELLOW}.git directory not found{colorama.Style.RESET_ALL}')


if __name__ == "__main__":
    consent = input(f'{colorama.Fore.YELLOW}Are you sure you want to '
                    f'delete the .git directory?{colorama.Style.RESET_ALL} '
                    f'{colorama.Fore.LIGHTBLUE_EX}(yes/no): {colorama.Style.RESET_ALL}')
    if consent.lower() == 'yes':
        remove_git_dir()
    else:
        print(f'{colorama.Fore.GREEN}No actions were taken{colorama.Style.RESET_ALL}')
