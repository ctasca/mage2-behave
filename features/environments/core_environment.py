import core_config.all as config
import re
from behave import use_fixture
from fixtures import *

def core_before_all(context):
    context.baseurl = config.DEVELOPMENT_ENV_BASEURL
    context.secure_baseurl = config.DEVELOPMENT_ENV_SECURE_BASEURL
    context.backend = config.DEVELOPMENT_BACKEND_URL

def core_before_feature(context, feature):
    if "fixture.splinter.browser.chrome" in feature.tags:
        use_fixture(splinter_browser_chrome, context)

    if "fixture.splinter.browser.chrome.fullscreen" in feature.tags:
        use_fixture(splinter_browser_chrome_fullscreen, context)

    if "fixture.splinter.browser.chrome.headless" in feature.tags:
        use_fixture(splinter_browser_chrome_headless, context)

    if "fixture.integration.admin.token" in feature.tags:
        use_fixture(integration_admin_token, context)

    if match := re.findall(r"(\bfixture.splinter.browser.chrome.screen.size.\b)+(\b[\d{0,}*\w{0,}*-{0,}?+]+\b)+", '|'.join(feature.tags)):
        for data in match:
            use_fixture(splinter_browser_chrome_screen_size, context, data[1])

def core_before_scenario(context, scenario):
    if "fixture.splinter.browser.chrome" in scenario.tags:
        use_fixture(splinter_browser_chrome, context)

    if "fixture.splinter.browser.chrome.fullscreen" in scenario.tags:
        use_fixture(splinter_browser_chrome_fullscreen, context)

    if "fixture.splinter.browser.chrome.headless" in scenario.tags:
        use_fixture(splinter_browser_chrome_headless, context)

    if "fixture.integration.admin.token" in scenario.tags:
        use_fixture(integration_admin_token, context)

    if match := re.findall(r"(\bfixture.splinter.browser.chrome.screen.size.\b)+(\b[\d{0,}*\w{0,}*-{0,}?+]+\b)+", '|'.join(scenario.tags)):
        for data in match:
            use_fixture(splinter_browser_chrome_screen_size, context, data[1])

