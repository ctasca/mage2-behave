import re
from features.fixtures import *
# noinspection PyPackageRequirements
from decouple import config
from features.core_config.bundle import context_development_environment


def core_before_all(context):
    context_development_environment(context, config)


def core_before_feature(context, feature):
    _take_screenshots(context, feature.tags)
    if "fixture.warden.maria.db.connect" in feature.tags:
        use_fixture(warden_maria_db_connect, context)
    _skip(context, feature, 'feature')
    _cleanup_screenshots(context, feature.tags, 'before')
    _set_environment(context, feature)
    _integration_admin_token(context, feature.tags)
    _dummy_customer_create(context, feature)
    _set_products_in_stock(context, feature)
    _set_products_out_of_stock(context, feature)


def core_before_scenario(context, scenario):
    _take_screenshots(context, scenario.tags)
    _skip(context, scenario, 'scenario')
    _cleanup_screenshots(context, scenario.tags, 'before')
    if "fixture.splinter.browser.chrome" in scenario.tags and not ('skip' in scenario.tags):
        use_fixture(splinter_browser_chrome, context)

    if "fixture.splinter.browser.chrome.fullscreen" in scenario.tags and not ('skip' in scenario.tags):
        use_fixture(splinter_browser_chrome_fullscreen, context)

    if "fixture.splinter.browser.chrome.headless" in scenario.tags and not ('skip' in scenario.tags):
        use_fixture(splinter_browser_chrome_headless, context)

    if matches := (_regex_fixture_tag_matches(scenario, 'fixture.splinter.browser.chrome.screen.size.') and
                   not ('skip' in scenario.tags)):
        for data in matches:
            use_fixture(splinter_browser_chrome_screen_size, context, data[1])
    _set_environment(context, scenario)
    _integration_admin_token(context, scenario.tags)
    _dummy_customer_create(context, scenario)
    _set_products_in_stock(context, scenario)
    _set_products_out_of_stock(context, scenario)


def core_after_scenario(context, scenario):
    _dummy_customer_delete(context, scenario)
    _cleanup_screenshots(context, scenario.tags, 'after')


def core_after_feature(context, feature):
    _dummy_customer_delete(context, feature)
    _cleanup_screenshots(context, feature.tags, 'after')


def _regex_fixture_tag_matches(hook, fixture_tag: str) -> list:
    return re.findall(rf"(\b{fixture_tag}\b)+(\b[\w*-?+]+\b)+", '|'.join(hook.tags))


def _take_screenshots(context, tags: list) -> None:
    if "fixture.take.screenshots" in tags:
        use_fixture(take_screenshots, context)


def _cleanup_screenshots(context, tags: list, hook: str) -> None:
    if "fixture.{}.cleanup.screenshots".format(hook) in tags:
        if hook == 'before':
            use_fixture(before_cleanup_screenshots, context)
        elif hook == 'after':
            use_fixture(after_cleanup_screenshots, context)


def _set_environment(context, hook) -> None:
    if matches := _regex_fixture_tag_matches(hook, 'fixture.set.environment.'):
        for data in matches:
            # Note: set_environment expects a string not a list.
            use_fixture(set_environment, context, data[1])


def _integration_admin_token(context, tags: list) -> None:
    """ Can be used both on before feature or scenario """
    if "fixture.integration.admin.token" in tags:
        use_fixture(integration_admin_token, context)


def _skip(context, hook, hook_type: str) -> None:
    if "skip" in hook.tags:
        message = (f"{colorama.Fore.LIGHTYELLOW_EX}Skipped {hook_type} due to 'skip' tag "
                   f"in {context.feature.filename} file{colorama.Style.RESET_ALL}")
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


def _set_products_in_stock(context, hook):
    use_fixture(integration_admin_token, context)
    if matches := _regex_fixture_tag_matches(hook, 'fixture.set.products.in.stock.'):
        for data in matches:
            use_fixture(set_products_in_stock, context, data[1])


def _set_products_out_of_stock(context, hook):
    use_fixture(integration_admin_token, context)
    if matches := _regex_fixture_tag_matches(hook, 'fixture.set.products.out.of.stock.'):
        for data in matches:
            use_fixture(set_products_out_of_stock, context, data[1])
