import core_config.all as config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from stere import Stere
from behave import *
from splinter import Browser, Config
from webdriver_manager.chrome import ChromeDriverManager

# Install chrome web driver by default
driver = ChromeDriverManager().install()

@fixture
def splinter_browser_chrome(context):
    # -- SETUP-FIXTURE PART:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("window-size=1920,1080")
    my_config = Config(fullscreen=False)
    service = Service(driver)
    browser = Browser('chrome', options=options, config=my_config, service=service)
    # configure Stere browser for Page objects
    Stere.browser = browser
    Stere.url_navigator = 'visit'
    context.browser = browser
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()

@fixture
def splinter_browser_chrome_fullscreen(context):
    # -- SETUP-FIXTURE PART:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    browser_config = Config(fullscreen=True)
    service = Service(driver)
    browser = Browser('chrome', options=options, config=browser_config, service=service)
    # configure Stere browser for Page objects
    Stere.browser = browser
    Stere.url_navigator = 'visit'
    context.browser = browser
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()

@fixture
def splinter_browser_chrome_screen_size(context, data):
    # -- SETUP-FIXTURE PART:
    width, height = data.split(':')
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("window-size={},{}".format(width, height))
    browser_config = Config(fullscreen=False)
    service = Service(driver)
    browser = Browser('chrome', options=options, config=browser_config, service=service)
    # configure Stere browser for Page objects
    Stere.browser = browser
    Stere.url_navigator = 'visit'
    context.browser = browser
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()