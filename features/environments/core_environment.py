import re
from features.core_config.core_config_baseurls import *
from features.core_config.core_config_backend import *
from features.fixtures import *
from colorama import Fore, Style


def core_before_all(context):
    context.baseurl = DEVELOPMENT_ENV_BASEURL
    context.secure_baseurl = DEVELOPMENT_ENV_SECURE_BASEURL
    context.backend = DEVELOPMENT_BACKEND_URL
    context.admin_username = DEVELOPMENT_ADMIN_USERNAME
    context.admin_password = DEVELOPMENT_ADMIN_PASSWORD


def core_before_feature(context, feature):
    _integration_admin_token(context, feature.tags)
    _skip(context, feature, 'feature')
    _dummy_customer_create(context, feature)


def core_before_scenario(context, scenario):
    if "fixture.splinter.browser.chrome" in scenario.tags:
        use_fixture(splinter_browser_chrome, context)

    if "fixture.splinter.browser.chrome.fullscreen" in scenario.tags:
        use_fixture(splinter_browser_chrome_fullscreen, context)

    if "fixture.splinter.browser.chrome.headless" in scenario.tags:
        use_fixture(splinter_browser_chrome_headless, context)

    if matches := _regex_fixture_tag_matches(scenario, 'fixture.splinter.browser.chrome.screen.size.'):
        for data in matches:
            use_fixture(splinter_browser_chrome_screen_size, context, data[1])

    _integration_admin_token(context, scenario.tags)
    _skip(context, scenario, 'scenario')
    _dummy_customer_create(context, scenario)


def core_after_scenario(context, scenario):
    _dummy_customer_delete(context, scenario)


def core_after_feature(context, feature):
    _dummy_customer_delete(context, feature)


def _regex_fixture_tag_matches(hook, fixture_tag: str) -> list:
    return re.findall(rf"(\b{fixture_tag}\b)+(\b[\w*-?+]+\b)+", '|'.join(hook.tags))


def _integration_admin_token(context, tags: list) -> None:
    """ Can be used both on before feature or scenario """
    if "fixture.integration.admin.token" in tags:
        use_fixture(integration_admin_token, context)


def _skip(context, hook, hook_type: str) -> None:
    if "skip" in hook.tags:
        message = (f"{Fore.LIGHTYELLOW_EX}Skipped {hook_type} due to 'skip' tag "
                   f"in {context.feature.filename} file{Style.RESET_ALL}")
        if hook_type == 'feature':
            hook.skip(message)
        if hook_type == 'scenario':
            hook.skip(message)
        return


def _dummy_customer_create(context, hook):
    """ Create a dummy customer via fixture tag @fixture.dummy.customer.create"""
    if "fixture.dummy.customer.create" in hook.tags:
        use_fixture(integration_admin_token, context)
        use_fixture(dummy_customer_create, context)


def _dummy_customer_delete(context, hook):
    """ Delete dummy customer via fixture tag @fixture.dummy.customer.delete"""
    if "fixture.dummy.customer.delete" in hook.tags:
        use_fixture(dummy_customer_delete, context)
