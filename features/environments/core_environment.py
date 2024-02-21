from features.core_config.config import *
import re
from features.fixtures import *


def core_before_all(context):
    context.baseurl = DEVELOPMENT_ENV_BASEURL
    context.secure_baseurl = DEVELOPMENT_ENV_SECURE_BASEURL
    context.backend = DEVELOPMENT_BACKEND_URL
    context.admin_username = DEVELOPMENT_ADMIN_USERNAME
    context.admin_password = DEVELOPMENT_ADMIN_PASSWORD


def core_before_feature(context, feature):
    _integration_admin_token(context, feature.tags)


def core_before_scenario(context, scenario):
    if "fixture.splinter.browser.chrome" in scenario.tags:
        use_fixture(splinter_browser_chrome, context)

    if "fixture.splinter.browser.chrome.fullscreen" in scenario.tags:
        use_fixture(splinter_browser_chrome_fullscreen, context)

    if "fixture.splinter.browser.chrome.headless" in scenario.tags:
        use_fixture(splinter_browser_chrome_headless, context)

    if match := re.findall(r"(\bfixture.splinter.browser.chrome.screen.size.\b)+(\b[\d{0,}*\w{0,}*-{0,}?+]+\b)+",
                           '|'.join(scenario.tags)):
        for data in match:
            use_fixture(splinter_browser_chrome_screen_size, context, data[1])

    _integration_admin_token(context, scenario.tags)


def _integration_admin_token(context, tags):
    """ Can be used both on before feature or scenario """
    if "fixture.integration.admin.token" in tags:
        use_fixture(integration_admin_token, context)
