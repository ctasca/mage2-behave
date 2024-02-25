import json
import requests
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from splinter import Browser, Config
from stere import Stere
from webdriver_manager.chrome import ChromeDriverManager
from features.core_config.core_config_baseurls import *
from features.core_config.core_config_backend import *
from features.core_config.dummy_customer import *
from colorama import Fore, Style

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
def set_environment(context, environment: str):
    switch = {
        'development': _set_development_environment,
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
        raise Exception(f'{Fore.RED}Unknown environment {environment}{Style.RESET_ALL}')



@fixture
def integration_admin_token(context):
    payload = {
        "username": context.admin_username,
        "password": context.admin_password
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post("{}rest/V1/integration/admin/token".format(context.baseurl), headers=headers,
                             data=json.dumps(payload))
    context.admin_token = response.json()
    yield context.admin_token


@fixture
def dummy_customer_create(context):
    """Note: when using this fixture the request for an admin token is automatically made"""
    payload = {
        "customer": {
            "email": CUSTOMER_USERNAME,
            "firstname": CUSTOMER_FIRSTNAME,
            "lastname": CUSTOMER_FIRSTNAME,
            "addresses": [{
                "defaultShipping": "true",
                "defaultBilling": "true",
                "firstname": CUSTOMER_FIRSTNAME,
                "lastname": CUSTOMER_LASTNAME,
                "region": CUSTOMER_ADDRESS_REGION,
                "postcode": CUSTOMER_ADDRESS_POSTCODE,
                "street": CUSTOMER_ADDRESS_STREET,
                "city": CUSTOMER_ADDRESS_CITY,
                "telephone": CUSTOMER_ADDRESS_TELEPHONE,
                "countryId": CUSTOMER_ADDRESS_COUNTRY_ID
            }]
        },
        "password": CUSTOMER_PASSWORD
    }
    headers = {"Content-Type": "application/json", "Authorization": "Bearer {}".format(context.admin_token)}
    response = requests.post("{}rest/V1/customers".format(context.baseurl), headers=headers,
                             data=json.dumps(payload))

    if response.status_code != 200:
        raise Exception('Could not create dummy customer')

    response_json = response.json()
    context.dummy_customer_id = response_json['id']
    yield context.dummy_customer_id


@fixture
def dummy_customer_delete(context):
    headers = {"Content-Type": "application/json", "Authorization": "Bearer {}".format(context.admin_token)}
    response = requests.delete(
        "{}rest/V1/customers/{}".format(context.baseurl, context.dummy_customer_id),
        headers=headers)

    if response.status_code != 200:
        raise Exception('Could not delete customer with ID {}'.format(context.dummy_customer_id))


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


def _set_development_environment(context):
    context.baseurl = DEVELOPMENT_ENV_BASEURL
    context.secure_baseurl = DEVELOPMENT_ENV_SECURE_BASEURL
    context.backend = DEVELOPMENT_BACKEND_URL
    context.admin_username = DEVELOPMENT_ADMIN_USERNAME
    context.admin_password = DEVELOPMENT_ADMIN_PASSWORD


def _set_integration_environment(context):
    context.baseurl = INTEGRATION_ENV_BASEURL
    context.secure_baseurl = INTEGRATION_ENV_SECURE_BASEURL
    context.backend = INTEGRATION_BACKEND_URL
    context.admin_username = INTEGRATION_ADMIN_USERNAME
    context.admin_password = INTEGRATION_ADMIN_PASSWORD


def _set_test_environment(context):
    context.baseurl = TEST_ENV_BASEURL
    context.secure_baseurl = TEST_ENV_SECURE_BASEURL
    context.backend = TEST_BACKEND_URL
    context.admin_username = TEST_ADMIN_USERNAME
    context.admin_password = TEST_ADMIN_PASSWORD


def _set_staging_environment(context):
    context.baseurl = STAGING_ENV_BASEURL
    context.secure_baseurl = STAGING_ENV_SECURE_BASEURL
    context.backend = STAGING_BACKEND_URL
    context.admin_username = STAGING_ADMIN_USERNAME
    context.admin_password = STAGING_ADMIN_PASSWORD


def _set_pre_production_environment(context):
    context.baseurl = PRE_PRODUCTION_ENV_BASEURL
    context.secure_baseurl = PRE_PRODUCTION_ENV_SECURE_BASEURL
    context.backend = PRE_PRODUCTION_BACKEND_URL
    context.admin_username = PRE_PRODUCTION_ADMIN_USERNAME
    context.admin_password = PRE_PRODUCTION_ADMIN_PASSWORD


def _set_production_environment(context):
    context.baseurl = PRODUCTION_ENV_BASEURL
    context.secure_baseurl = PRODUCTION_ENV_SECURE_BASEURL
    context.backend = PRODUCTION_BACKEND_URL
    context.admin_username = PRODUCTION_ADMIN_USERNAME
    context.admin_password = PRODUCTION_ADMIN_PASSWORD
