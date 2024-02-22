# remove_git.py
"""
This script should be used to drop the mage2-behave git repository from the current working directory,
in order to include the project as part of the Magento 2 repository.
"""
import os
import shutil
from colorama import Fore, Style

print(f'{Fore.YELLOW}WARNING:{Style.RESET_ALL} '
      f'{Fore.RED}This action will delete the .git directory and cannot be undone.{Style.RESET_ALL}')


def remove_git_dir():
    git_dir = os.path.join(os.getcwd(), '.git')
    if os.path.exists(git_dir):
        print(f'Removing {git_dir}...')
        shutil.rmtree(git_dir)
        print(f'{Fore.GREEN}Successfully removed .git directory{Style.RESET_ALL}')
    else:
        print(f'{Fore.YELLOW}.git directory not found{Style.RESET_ALL}')


if __name__ == "__main__":
    consent = input(f'{Fore.YELLOW}Are you sure you want to delete the .git directory?{Style.RESET_ALL} '
                    f'{Fore.LIGHTBLUE_EX}(yes/no): {Style.RESET_ALL}')
    if consent.lower() == 'yes':
        remove_git_dir()
    else:
        print(f'{Fore.GREEN}No actions were taken{Style.RESET_ALL}')
