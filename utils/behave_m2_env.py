import os
import shutil
import fileinput
from utils.docker_env import docker_bin_magento

script_directory = os.path.dirname(__file__)
directory_path = os.path.join(script_directory, '..', '..', 'mage2-behave')

absolute_path = os.path.abspath(directory_path)

parent_directory = os.path.dirname(absolute_path)
app_etc_directory = os.path.join(parent_directory, os.path.join('app', 'etc'))
env_file = os.path.join(app_etc_directory, 'env.php')
env_orig_file = os.path.join(app_etc_directory, 'env.php.orig')
env_behave_file = os.path.join(app_etc_directory, 'env.php.behave')


def copy_and_modify_env_db_data(context):
    # copy the file
    shutil.copy(env_file, env_orig_file)

    with fileinput.input(files=env_file, inplace=True) as f:
        for line in f:
            print(line.replace(
                f"'dbname' => '{context.db_name}'",
                f"'dbname' => '{context.db_test_name}'"
            ).replace(
                f"'username' => '{context.db_user}'",
                f"'username' => '{context.db_root_user}'"
            ), end='')


def reset_env_db_data(context):
    shutil.copy(env_file, env_behave_file)
    shutil.copy(env_orig_file, env_file)
    if os.path.exists(env_behave_file) and os.path.isfile(env_behave_file):
        os.remove(env_orig_file)
        os.remove(env_behave_file)
