import json
import requests
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from splinter import Browser, Config
from stere import Stere
from webdriver_manager.chrome import ChromeDriverManager
from features.core_config.dummy_customer import *

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
