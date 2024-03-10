import json
import requests
import colorama
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from splinter import Browser, Config
from stere import Stere
from webdriver_manager.chrome import ChromeDriverManager
# noinspection PyPackageRequirements
from decouple import config
from core_config.bundle import config_parser, SECTIONS, context_development_environment
from utils.screenshot import cleanup

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
def before_cleanup_screenshots(context):
    _clean_screenshots()


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
                             data=json.dumps(payload))
    context.admin_token = response.json()
    yield context.admin_token


@fixture
def dummy_customer_create(context):
    """Note: when using this fixture the request for an admin token is automatically made"""
    payload = {
        "customer": {
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
    response = requests.post(f"{context.baseurl}{customers_rest_path}", headers=headers, data=json.dumps(payload))
    if response.status_code != 200:
        raise Exception('Could not create dummy customer')
    response_json = response.json()
    context.dummy_customer_id = response_json['id']
    yield context.dummy_customer_id


@fixture
def dummy_customer_delete(context):
    headers = {"Content-Type": "application/json", "Authorization": "Bearer {}".format(context.admin_token)}
    response = requests.delete(
        "{}{}{}".format(context.baseurl, config_parser.get(SECTIONS.get('api'), 'CUSTOMERS_REST_PATH'),
                        context.dummy_customer_id), headers=headers)

    if response.status_code != 200:
        raise Exception('Could not delete customer with ID {}'.format(context.dummy_customer_id))


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
        response = requests.put(endpoint, headers=headers, data=json.dumps(payload))
        if response.status_code != 200:
            raise Exception('Could not update product stock status')


def _init_context_browser(context, browser_config: Config, custom_size=None) -> None:
    width, height = '1920', '1080'
    if custom_size is not None:
        width, height = custom_size.split(':')
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("window-size={},{}".format(width, height))
    my_config = browser_config
    service = Service(driver)
    browser = Browser('chrome', options=options, config=my_config, service=service)
    # configure Stere browser for Page objects
    Stere.browser = browser
    Stere.url_navigator = 'visit'
    context.browser = browser


def _clean_screenshots() -> None:
    """ Clean up the screenshots directory """
    cleanup()


def _set_development_environment(context):
    context_development_environment(context, config)


def _set_integration_environment(context):
    context.baseurl = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_ENV_BASEURL')
    context.secure_baseurl = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_ENV_SECURE_BASEURL')
    context.backend = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_BACKEND_URL')
    context.admin_username = config_parser.get(SECTIONS.get('integration'), 'INTEGRATION_ADMIN_USERNAME')
    context.admin_password = config('integration_admin_password')


def _set_test_environment(context):
    context.baseurl = config_parser.get(SECTIONS.get('test'), 'TEST_ENV_BASEURL')
    context.secure_baseurl = config_parser.get(SECTIONS.get('test'), 'TEST_ENV_SECURE_BASEURL')
    context.backend = config_parser.get(SECTIONS.get('test'), 'TEST_BACKEND_URL')
    context.admin_username = config_parser.get(SECTIONS.get('test'), 'TEST_ADMIN_USERNAME')
    context.admin_password = config('test_admin_password')


def _set_staging_environment(context):
    context.baseurl = config_parser.get(SECTIONS.get('stage'), 'STAGING_ENV_BASEURL')
    context.secure_baseurl = config_parser.get(SECTIONS.get('stage'), 'STAGING_ENV_SECURE_BASEURL')
    context.backend = config_parser.get(SECTIONS.get('stage'), 'STAGING_BACKEND_URL')
    context.admin_username = config_parser.get(SECTIONS.get('stage'), 'STAGING_ADMIN_USERNAME')
    context.admin_password = config('staging_admin_password')


def _set_pre_production_environment(context):
    context.baseurl = config_parser.get(SECTIONS.get('pre_prod'), 'PRE_PRODUCTION_ENV_BASEURL')
    context.secure_baseurl = config_parser.get(SECTIONS.get('pre_prod'), 'PRE_PRODUCTION_ENV_SECURE_BASEURL')
    context.backend = config_parser.get(SECTIONS.get('pre_prod'), 'PRE_PRODUCTION_BACKEND_URL')
    context.admin_username = config_parser.get(SECTIONS.get('pre_prod'), 'PRE_PRODUCTION_ADMIN_USERNAME')
    context.admin_password = config('pre_production_admin_password')


def _set_production_environment(context):
    context.baseurl = config_parser.get(SECTIONS.get('prod'), 'PRODUCTION_ENV_BASEURL')
    context.secure_baseurl = config_parser.get(SECTIONS.get('prod'), 'PRODUCTION_ENV_SECURE_BASEURL')
    context.backend = config_parser.get(SECTIONS.get('prod'), 'PRODUCTION_BACKEND_URL')
    context.admin_username = config_parser.get(SECTIONS.get('prod'), 'PRODUCTION_ADMIN_USERNAME')
    context.admin_password = config('production_admin_password')
