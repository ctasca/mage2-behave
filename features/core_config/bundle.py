import configparser
import os

from typing import Dict

SECTIONS: Dict[str, str] = {
    "dev": "Development",
    "integration": "Integration",
    "test": "Test",
    "stage": "Staging",
    "pre_prod": "PreProduction",
    "prod": "Production",
    "customer": "DummyCustomer",
    "api": "Api",
    "docker": "Docker"
}

config_parser = configparser.ConfigParser()
current_dir = os.path.dirname(os.path.abspath(__file__))

config_parser.read(os.path.join(current_dir, 'core_config_baseurls.ini'))
config_parser.read(os.path.join(current_dir, 'core_config_backend.ini'))
config_parser.read(os.path.join(current_dir, 'dummy_customer.ini'))
config_parser.read(os.path.join(current_dir, 'docker_config.ini'))
config_parser.read(os.path.join(current_dir, 'api.ini'))
config_parser.read(os.path.join(current_dir, 'db_config.ini'))


def context_development_environment(context, config):
    context.baseurl = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_ENV_BASEURL')
    context.secure_baseurl = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_ENV_SECURE_BASEURL')
    context.backend = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_BACKEND_URL')
    context.admin_username = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_ADMIN_USERNAME')
    context.admin_password = config('development_admin_password')
    context.db_host = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_DB_HOST')
    context.db_port = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_DB_PORT')
    context.db_user = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_DB_USER')
    context.db_root_user = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_DB_ROOT_USER')
    context.db_name = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_DB_NAME')
    context.db_connection_timeout = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_DB_CONNECTION_TIMEOUT')
    context.db_read_timeout = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_DB_READ_TIMEOUT')
    context.db_write_timeout = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_DB_WRITE_TIMEOUT')
    context.db_remote_bind_address_host = config_parser.get(SECTIONS.get('dev'),
                                                            'DEVELOPMENT_DB_REMOTE_BIND_ADDRESS_HOST')
    context.db_remote_host_port = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_DB_REMOTE_HOST_PORT')
    context.db_password = config('development_db_password')
    context.db_root_password = config('development_db_root_password')
    context.warden_tunnel_ssh_key = config_parser.get(SECTIONS.get('docker'), 'WARDEN_TUNNEL_SSH_KEY')
    context.warden_tunnel_ssh_host = config_parser.get(SECTIONS.get('docker'), 'WARDEN_TUNNEL_SSH_HOST')
    context.warden_tunnel_ssh_user = config_parser.get(SECTIONS.get('docker'), 'WARDEN_TUNNEL_SSH_USER')
    context.warden_tunnel_ssh_port = config_parser.get(SECTIONS.get('docker'), 'WARDEN_TUNNEL_SSH_PORT')
    context.db_test_name = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_DB_TEST_NAME')
