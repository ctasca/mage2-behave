import configparser
import os

SECTIONS: dict[str, str] = {
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


def context_development_environment(context, config):
    context.baseurl = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_ENV_BASEURL')
    context.secure_baseurl = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_ENV_SECURE_BASEURL')
    context.backend = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_BACKEND_URL')
    context.admin_username = config_parser.get(SECTIONS.get('dev'), 'DEVELOPMENT_ADMIN_USERNAME')
    context.admin_password = config('development_admin_password')
