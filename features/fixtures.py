import os
import json
import mariadb
import requests
import colorama
import paramiko
from os.path import expanduser
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from splinter import Browser, Config
from stere import Stere
from webdriver_manager.chrome import ChromeDriverManager
from sshtunnel import SSHTunnelForwarder
from core_config.bundle import (config_parser, SECTIONS, context_development_environment, test_products_dictionary,
                                test_products_skus_array)
from utils import screenshots, docker_env, stores
# noinspection PyPackageRequirements
from decouple import config
from mariadb.connections import Connection

# Install Chrome web driver by default
driver = ChromeDriverManager().install()


@fixture
def splinter_browser_chrome(context):
    # -- SETUP-FIXTURE PART:
    _init_context_browser(context, Config(fullscreen=False))
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


@fixture
def splinter_browser_chrome_incognito(context):
    # -- SETUP-FIXTURE PART:
    _init_context_browser(context, Config(fullscreen=False), incognito=True)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


@fixture
def splinter_browser_chrome_fullscreen(context):
    # -- SETUP-FIXTURE PART:
    _init_context_browser(context, Config(fullscreen=True))
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


@fixture
def splinter_browser_chrome_screen_size(context, data):
    _init_context_browser(context, Config(fullscreen=False), data)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


@fixture
def splinter_browser_chrome_headless(context):
    # -- SETUP-FIXTURE PART:
    _init_context_browser(context, Config(headless=True))
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


@fixture
def splinter_browser_chrome_headless_incognito(context):
    # -- SETUP-FIXTURE PART:
    _init_context_browser(context, Config(headless=True), incognito=True)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


@fixture
def maria_db_connect(context):
    """
    Connection is made to configured test database name via root user and password
    """
    try:
        conn = _maria_db_connection(context, int(context.db_port))
        context.conn = conn
        yield context.conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        context.conn.cursor().close()
        context.conn.close()


@fixture
def warden_maria_db_connect(context):
    """
    Connection is made to configured test database name via root user and password
    """
    server = None
    try:
        home = expanduser("~")
        pkey = paramiko.RSAKey.from_private_key_file(os.path.join(home, context.warden_tunnel_ssh_key))
        ssh_host = context.warden_tunnel_ssh_host
        ssh_user = context.warden_tunnel_ssh_user
        ssh_port = int(context.db_remote_host_port)
        remote_db_host = docker_env.container_name_search(context.db_remote_bind_address_host)
        server = SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_pkey=pkey,
            remote_bind_address=(remote_db_host, int(context.db_port)),
            set_keepalive=100000
        )
        server.start()
        conn = _maria_db_connection(context, int(server.local_bind_port))
        context.conn = conn
        yield context.conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        context.conn.cursor().close()
        context.conn.close()
        server.stop()


@fixture
def take_screenshots(context):
    context.take_screenshots = True


@fixture
def setup_upgrade(context):
    docker_env.docker_bin_magento('setup:upgrade')


# noinspection PyUnusedLocal
@fixture
def before_cleanup_screenshots(context):
    _clean_screenshots()


# noinspection PyUnusedLocal
@fixture
def after_cleanup_screenshots(context):
    _clean_screenshots()


@fixture
def set_environment(context, environment: str):
    switch = {
        SECTIONS.get('dev'): _set_development_environment,
        'integration': _set_integration_environment,
        'test': _set_test_environment,
        'staging': _set_staging_environment,
        'pre_production': _set_pre_production_environment,
        'production': _set_production_environment
    }
    try:
        func = switch.get(environment)
        func(context)
    except Exception:
        raise Exception(f'{colorama.Fore.RED}Unknown environment {environment}{colorama.Style.RESET_ALL}')


@fixture
def integration_admin_token(context):
    payload = {
        "username": context.admin_username,
        "password": context.admin_password
    }
    integration_admin_token_path = config_parser.get(SECTIONS.get('api'), 'ADMIN_INTEGRATION_TOKEN_REST_PATH')
    headers = {"Content-Type": "application/json"}
    response = requests.post("{}{}".format(context.baseurl, integration_admin_token_path), headers=headers,
                             data=json.dumps(payload), verify=False)
    context.admin_token = response.json()
    yield context.admin_token


@fixture
def dummy_customer_create(context, dummy_customer_delete, data):
    """Note: when using this fixture the request for an admin token is automatically made"""
    payload = {
        "customer": {
            "store_id": context.stores[data],
            "email": config_parser.get(SECTIONS.get('customer'), 'CUSTOMER_USERNAME'),
            "firstname": config_parser.get(SECTIONS.get('customer'), 'CUSTOMER_FIRSTNAME'),
            "lastname": config_parser.get(SECTIONS.get('customer'), 'CUSTOMER_LASTNAME'),
            "addresses": [{
                "defaultShipping": "true",
                "defaultBilling": "true",
                "firstname": config_parser.get(SECTIONS.get('customer'), 'CUSTOMER_FIRSTNAME'),
                "lastname": config_parser.get(SECTIONS.get('customer'), 'CUSTOMER_LASTNAME'),
                "region": json.loads(config_parser.get(SECTIONS.get('customer'), 'CUSTOMER_ADDRESS_REGION')),
                "postcode": config_parser.get(SECTIONS.get('customer'), 'CUSTOMER_ADDRESS_POSTCODE'),
                "street": json.loads(config_parser.get(SECTIONS.get('customer'), 'CUSTOMER_ADDRESS_STREET')),
                "city": config_parser.get(SECTIONS.get('customer'), 'CUSTOMER_ADDRESS_CITY'),
                "telephone": config_parser.get(SECTIONS.get('customer'), 'CUSTOMER_ADDRESS_TELEPHONE'),
                "countryId": config_parser.get(SECTIONS.get('customer'), 'CUSTOMER_ADDRESS_COUNTRY_ID')
            }]
        },
        "password": config('customer_password')
    }
    headers = {"Content-Type": "application/json", "Authorization": "Bearer {}".format(context.admin_token)}
    customers_rest_path = config_parser.get(SECTIONS.get('api'), 'CUSTOMERS_REST_PATH')
    response = requests.post(f"{context.baseurl}{customers_rest_path}", headers=headers, data=json.dumps(payload),
                             verify=False)
    if response.status_code != 200:
        raise Exception('Could not create dummy customer')
    response_json = response.json()
    context.dummy_customer_id = response_json['id']
    yield context.dummy_customer_id
    # -- CLEANUP-FIXTURE PART:
    use_fixture(dummy_customer_delete, context)


@fixture
def dummy_customer_create_in_website(context, dummy_customer_delete, data):
    email = config_parser.get(SECTIONS.get('customer'), 'CUSTOMER_USERNAME')
    password = config('customer_password')
    payload = {
        "customer": {
            "website_id": context.stores[data],
            "email": email,
        },
        "password": password
    }
    headers = {"Content-Type": "application/json", "Authorization": "Bearer {}".format(context.admin_token)}
    customers_rest_path = config_parser.get(SECTIONS.get('api'), 'CUSTOMERS_REST_PATH')
    response = requests.post(f"{context.baseurl}{customers_rest_path}", headers=headers, data=json.dumps(payload),
                             verify=False)
    if response.status_code != 200:
        raise Exception('Could not create dummy customer')
    response_json = response.json()
    context.dummy_customer_id = response_json['id']
    context.dummy_customer_email = email
    context.dummy_customer_password = password
    try:
        cur = context.conn.cursor()
        cur.execute(
            "UPDATE customer_entity SET confirmation = NULL WHERE entity_id = {}".format(context.dummy_customer_id)
        )
        context.conn.commit()
    except mariadb.Error:
        context.conn.rollback()
    yield context.dummy_customer_id, context.dummy_customer_email, context.dummy_customer_password
    # -- CLEANUP-FIXTURE PART:
    use_fixture(dummy_customer_delete, context)


@fixture
def dummy_customer_delete(context):
    headers = {"Content-Type": "application/json", "Authorization": "Bearer {}".format(context.admin_token)}
    response = requests.delete(
        "{}{}{}".format(context.baseurl, config_parser.get(SECTIONS.get('api'), 'CUSTOMERS_REST_PATH'),
                        context.dummy_customer_id), headers=headers, verify=False)

    if response.status_code != 200:
        raise Exception('Could not delete customer with ID {}'.format(context.dummy_customer_id))


# noinspection PyUnusedLocal
@fixture
def skip(context):
    pass


@fixture
def set_products_in_stock(context, data):
    """Note: when using this fixture the request for an admin token is automatically made"""
    _set_product_is_in_stock_request(context, data, 'true')


@fixture
def set_products_out_of_stock(context, data):
    """Note: when using this fixture the request for an admin token is automatically made"""
    _set_product_is_in_stock_request(context, data, 'false')


def set_stores_dictionary(context):
    stores_dictionary = stores.dictionary(context)
    context.stores = stores_dictionary
    yield context.stores


def _set_product_is_in_stock_request(context, data, is_in_stock: str):
    skus = data.split(":")
    api_endpoint_uri_format = "{}{}".format(context.baseurl,
                                            config_parser.get(SECTIONS.get('api'), 'PRODUCTS_REST_PATH'), context)
    for sku in skus:
        endpoint = "{}{}".format(api_endpoint_uri_format, sku)
        payload = {
            "product": {
                "extension_attributes": {
                    "stock_item": {
                        "is_in_stock": is_in_stock
                    }
                }
            }
        }
        headers = {'Authorization': 'Bearer {} '.format(context.admin_token), "Content-Type": "application/json"}
        response = requests.put(endpoint, headers=headers, data=json.dumps(payload), verify=False)
        if response.status_code != 200:
            raise Exception('Could not update product stock status')


def _init_context_browser(context, browser_config: Config,
                          custom_size=None, incognito=False, enable_automation=True) -> None:
    width, height = '1920', '1080'
    if custom_size is not None:
        width, height = custom_size.split(':')
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    if incognito:
        options.add_argument('--incognito')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--enable-javascript")
    options.add_argument("--enable-file-cookies")
    options.add_argument("window-size={},{}".format(width, height))
    if enable_automation:
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
    my_config = browser_config
    service = Service(wait_time=3)
    browser = Browser('chrome', options=options, config=my_config, service=service)
    # configure Stere browser for Page objects
    Stere.browser = browser
    Stere.url_navigator = 'visit'
    context.browser = browser


def _clean_screenshots() -> None:
    """ Clean up the screenshots directory """
    screenshots.cleanup()


def _maria_db_connection(context, db_port: int) -> Connection:
    return mariadb.connect(
        user=context.db_root_user,
        password=context.db_root_password,
        host=context.db_host,
        port=db_port,
        database=context.db_test_name,
        connect_timeout=int(context.db_connection_timeout),
        read_timeout=int(context.db_read_timeout),
        write_timeout=int(context.db_write_timeout)
    )


def _set_development_environment(context):
    context_development_environment(context, config)


def _set_integration_environment(context):
    context.baseurl = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_ENV_BASEURL')
    context.secure_baseurl = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_ENV_SECURE_BASEURL')
    context.backend = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_BACKEND_URL')
    context.admin_username = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_ADMIN_USERNAME')
    context.admin_password = config('integration_admin_password')
    context.db_host = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_DB_HOST')
    context.db_port = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_DB_PORT')
    context.db_user = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_DB_USER')
    context.db_root_user = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_DB_ROOT_USER')
    context.db_connection_timeout = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_DB_CONNECTION_TIMEOUT')
    context.db_read_timeout = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_DB_READ_TIMEOUT')
    context.db_write_timeout = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_DB_WRITE_TIMEOUT')
    context.db_remote_bind_address_host = config_parser.get(SECTIONS.get('integration'),
                                                            'INTEGRATION_DB_REMOTE_BIND_ADDRESS_HOST')
    context.db_remote_host_port = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_DB_REMOTE_HOST_PORT')
    context.db_password = config('integration_db_password')
    context.db_root_password = config('integration_db_root_password')
    context.persistent_customer = config_parser.get(SECTIONS.get('persistent_customer'), 'CUSTOMER_USERNAME')
    context.persistent_customer_password = config('persistent_customer_password')
    test_products = config_parser.get(SECTIONS.get('integration'), 'TEST_PRODUCTS')
    if test_products:
        context.test_products = test_products_dictionary(test_products)
        context.test_products_skus = test_products_skus_array(test_products)



def _set_test_environment(context):
    context.baseurl = config_parser.get(SECTIONS.get('test'), 'TEST_ENV_BASEURL')
    context.secure_baseurl = config_parser.get(SECTIONS.get('test'), 'TEST_ENV_SECURE_BASEURL')
    context.backend = config_parser.get(SECTIONS.get('test'), 'TEST_BACKEND_URL')
    context.admin_username = config_parser.get(SECTIONS.get('test'), 'TEST_ADMIN_USERNAME')
    context.admin_password = config('test_admin_password')
    context.db_host = config_parser.get(SECTIONS.get('test'), 'TEST_DB_HOST')
    context.db_port = config_parser.get(SECTIONS.get('test'), 'TEST_DB_PORT')
    context.db_user = config_parser.get(SECTIONS.get('test'), 'TEST_DB_USER')
    context.db_root_user = config_parser.get(SECTIONS.get('test'), 'TEST_DB_ROOT_USER')
    context.db_connection_timeout = config_parser.get(SECTIONS.get('test'), 'TEST_DB_CONNECTION_TIMEOUT')
    context.db_read_timeout = config_parser.get(SECTIONS.get('test'), 'TEST_DB_READ_TIMEOUT')
    context.db_write_timeout = config_parser.get(SECTIONS.get('test'), 'TEST_DB_WRITE_TIMEOUT')
    context.db_remote_bind_address_host = config_parser.get(SECTIONS.get('test'),
                                                            'TEST_DB_REMOTE_BIND_ADDRESS_HOST')
    context.db_remote_host_port = config_parser.get(SECTIONS.get('test'), 'TEST_DB_REMOTE_HOST_PORT')
    context.db_password = config('test_db_password')
    context.db_root_password = config('test_db_root_password')
    context.persistent_customer = config_parser.get(SECTIONS.get('persistent_customer'), 'CUSTOMER_USERNAME')
    context.persistent_customer_password = config('persistent_customer_password')
    test_products = config_parser.get(SECTIONS.get('test'), 'TEST_PRODUCTS')
    if test_products:
        context.test_products = test_products_dictionary(test_products)
        context.test_products_skus = test_products_skus_array(test_products)


def _set_staging_environment(context):
    context.baseurl = config_parser.get(SECTIONS.get('stage'), 'STAGING_ENV_BASEURL')
    context.secure_baseurl = config_parser.get(SECTIONS.get('stage'), 'STAGING_ENV_SECURE_BASEURL')
    context.backend = config_parser.get(SECTIONS.get('stage'), 'STAGING_BACKEND_URL')
    context.admin_username = config_parser.get(SECTIONS.get('stage'), 'STAGING_ADMIN_USERNAME')
    context.admin_password = config('staging_admin_password')
    context.db_host = config_parser.get(SECTIONS.get('stage'), 'STAGING_DB_HOST')
    context.db_port = config_parser.get(SECTIONS.get('stage'), 'STAGING_DB_PORT')
    context.db_user = config_parser.get(SECTIONS.get('stage'), 'STAGING_DB_USER')
    context.db_root_user = config_parser.get(SECTIONS.get('stage'), 'STAGING_DB_ROOT_USER')
    context.db_connection_timeout = config_parser.get(SECTIONS.get('stage'), 'STAGING_DB_CONNECTION_TIMEOUT')
    context.db_read_timeout = config_parser.get(SECTIONS.get('stage'), 'STAGING_DB_READ_TIMEOUT')
    context.db_write_timeout = config_parser.get(SECTIONS.get('stage'), 'STAGING_DB_WRITE_TIMEOUT')
    context.db_remote_bind_address_host = config_parser.get(SECTIONS.get('stage'),
                                                            'STAGING_DB_REMOTE_BIND_ADDRESS_HOST')
    context.db_remote_host_port = config_parser.get(SECTIONS.get('stage'), 'STAGING_DB_REMOTE_HOST_PORT')
    context.db_password = config('staging_db_password')
    context.db_root_password = config('staging_db_root_password')
    context.persistent_customer = config_parser.get(SECTIONS.get('persistent_customer'), 'CUSTOMER_USERNAME')
    context.persistent_customer_password = config('persistent_customer_password')
    test_products = config_parser.get(SECTIONS.get('stage'), 'TEST_PRODUCTS')
    if test_products:
        context.test_products = test_products_dictionary(test_products)
        context.test_products_skus = test_products_skus_array(test_products)



def _set_pre_production_environment(context):
    context.baseurl = config_parser.get(SECTIONS.get('pre_prod'), 'PRE_PRODUCTION_ENV_BASEURL')
    context.secure_baseurl = config_parser.get(SECTIONS.get('pre_prod'), 'PRE_PRODUCTION_ENV_SECURE_BASEURL')
    context.backend = config_parser.get(SECTIONS.get('pre_prod'), 'PRE_PRODUCTION_BACKEND_URL')
    context.admin_username = config_parser.get(SECTIONS.get('pre_prod'), 'PRE_PRODUCTION_ADMIN_USERNAME')
    context.admin_password = config('pre_production_admin_password')
    context.persistent_customer = config_parser.get(SECTIONS.get('persistent_customer'), 'CUSTOMER_USERNAME')
    context.persistent_customer_password = config('persistent_customer_password')
    test_products = config_parser.get(SECTIONS.get('pre_prod'), 'TEST_PRODUCTS')
    if test_products:
        context.test_products = test_products_dictionary(test_products)
        context.test_products_skus = test_products_skus_array(test_products)


def _set_production_environment(context):
    """
    NOTE: IN PRODUCTION ENVIRONMENT ONLY THE MAGENTO BASE URL AND SECURE BASE URL CAN BE SET
    """
    context.baseurl = config_parser.get(SECTIONS.get('prod'), 'PRODUCTION_ENV_BASEURL')
    context.secure_baseurl = config_parser.get(SECTIONS.get('prod'), 'PRODUCTION_ENV_SECURE_BASEURL')
