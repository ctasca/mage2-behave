import os
import subprocess
from features.core_config.bundle import SECTIONS, config_parser
from utils.docker_env import container_id_search
from datetime import datetime
# noinspection PyPackageRequirements
from decouple import config

# Specifying the Docker container name or id
container_id = container_id_search(config_parser.get(SECTIONS.get('docker'), 'DB_SERVICE'))

db_name = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_DB_NAME')
db_user = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_DB_USER')
db_password = config('development_db_password')
now = datetime.now()
date_time_str = now.strftime("%Y-%m-%d_%H-%M-%S")
dump_file_name = f'dump_{date_time_str}.sql'
tests_db_name = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_DB_TEST_NAME')
dumps_dir = git_dir = os.path.join(os.getcwd(), 'dumps')
dump_abs_path = os.path.join(dumps_dir, dump_file_name)


def _dump_database():
    dump_command = (f"docker exec {container_id} "
                    f"mysqldump -u {db_user} -p{db_password} {db_name} > '/tmp/{dump_file_name}'")
    subprocess.run(dump_command, shell=True)


def _copy_dump_to_project():
    copy_command = f"cp /tmp/{dump_file_name} {dump_abs_path}"
    subprocess.run(copy_command, shell=True)
    rm_command = f"rm /tmp/{dump_file_name}"
    subprocess.run(rm_command, shell=True)


def _create_database_and_import_dump(new_db_name):
    drop_db_command = (f"docker exec {container_id} mysql -u{db_user} -p{db_password} -e "
                       f"'DROP DATABASE IF EXISTS {new_db_name};'")
    subprocess.run(drop_db_command, shell=True)
    # Command to create a new database
    create_db_command = (f"docker exec {container_id} mysql -u{db_user} -p{db_password} -e "
                         f"'CREATE DATABASE {new_db_name};'")
    subprocess.run(create_db_command, shell=True)

    # Command to import dump into the newly created database
    import_dump_command = (f"docker exec -i {container_id} mysql -u{db_user} -p{db_password} {new_db_name} "
                           f"< {dump_abs_path}")
    subprocess.run(import_dump_command, shell=True)

    rm_command = f"rm {dump_abs_path}"
    subprocess.run(rm_command, shell=True)


def execute():
    _dump_database()
    _copy_dump_to_project()
    _create_database_and_import_dump(tests_db_name)