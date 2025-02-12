import os
import shutil
import fileinput
import sys
from colorama import Fore, Style
from .confirmation import yes_no_input

script_directory = os.path.dirname(__file__)
mage2_directory = os.path.join(script_directory, '..', '..', 'mage2-behave')
bck_path = os.path.join(script_directory, '..', 'bck')
mage2_behave_path = os.path.abspath(mage2_directory)
parent_directory = os.path.dirname(mage2_behave_path)
app_etc_directory = os.path.join(parent_directory, os.path.join('app', 'etc'))
env_file = os.path.join(app_etc_directory, 'env.php')
env_bck_file = os.path.join(bck_path, 'env.php.bck')
env_orig_file = os.path.join(app_etc_directory, 'env.php.orig.behave')
behave_flag = os.path.join(app_etc_directory, 'behave.flag')


def copy_and_modify_env_db_data(context):
    if not os.path.exists(env_file) and not os.path.isfile(env_file):
        raise Exception('env.php file could not be found!')

    shutil.copy(env_file, env_orig_file)
    shutil.copy(env_file, env_bck_file)

    with open(behave_flag, 'w') as file:
        file.write("# Behave flag file")

    with fileinput.input(files=env_file, inplace=True) as file:
        for line in file:
            print(line.replace(
                f"'dbname' => '{context.db_name}'",
                f"'dbname' => '{context.db_test_name}'"
            ).replace(
                f"'username' => '{context.db_user}'",
                f"'username' => '{context.db_root_user}'"
            ), end='')


def reset_env_db_data():
    shutil.copy(env_orig_file, env_file)
    if ((os.path.exists(behave_flag) and os.path.isfile(behave_flag)) or
            (os.path.exists(env_orig_file) and os.path.isfile(env_orig_file))):
        os.remove(env_orig_file)
        os.remove(behave_flag)


def verify_env():
    if os.path.exists(env_orig_file) and os.path.isfile(env_orig_file):
        print(f'{Fore.RED}env.php.orig.behave file exists! Aborting behave...{Style.RESET_ALL}')
        reset = yes_no_input('Do you want to reset the environment files?')
        if reset:
            reset_env_db_data()
            print(f'{Fore.GREEN}env.php.orig.behave and behave.flag successfully removed{Style.RESET_ALL}')
        sys.exit(1)
