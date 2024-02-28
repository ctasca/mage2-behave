import subprocess
import docker
import re
from docker.client import DockerClient
from features.core_config.bundle import config_parser, SECTIONS


def client() -> DockerClient:
    return docker.from_env()


def container_id_search(search: str) -> str:
    docker_client = docker.from_env()
    containers = docker_client.containers.list()
    for container in containers:
        if re.search(search, container.name):
            return container.id
    raise Exception("No {} container match".format(search))


def docker_bin_magento(command: str):
    magento_php_fom_service = config_parser.get(SECTIONS.get('docker'), 'PHP_FPM_SERVICE')
    container_id = container_id_search(magento_php_fom_service)
    command = 'bin/magento {}'.format(command)
    full_command = f"docker exec {container_id} {command}"
    process = subprocess.Popen(full_command, shell=True)
    process.wait()
    return
