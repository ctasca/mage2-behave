from selenium.common.exceptions import WebDriverException, ElementClickInterceptedException
from stere.fields import Field, Link
from features.core_config.backend.locators.system_configuration import *


class SystemConfigurationTab(Field):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)

    @staticmethod
    def get_tab_link(link_text: str) -> Link:
        return Link(TAB_LINK_LOCATOR_FORMAT[STRATEGY_KEY], TAB_LINK_LOCATOR_FORMAT[LOCATOR_KEY].format(link_text))

    @staticmethod
    def get_tab_group_link(link_text: str) -> Link:
        return Link(TAB_GROUP_LINK_LOCATOR_FORMAT[STRATEGY_KEY],
                    TAB_GROUP_LINK_LOCATOR_FORMAT[LOCATOR_KEY].format(link_text))

    def click_tab_link(self, link_text: str) -> Link:
        link = self.get_tab_link(link_text)
        try:
            assert link.is_clickable(10) and link.is_visible(10)
            is_active = link.find_by_xpath('../..').has_class('_active')
            # do not click if already active
            if not is_active:
                link.click()
            return link
        except (WebDriverException, ElementClickInterceptedException, AssertionError):
            raise Exception("Could not click tab link with text '{}'".format(link_text))

    def click_tab_group_link(self, link_text: str) -> Link:
        link = self.get_tab_group_link(link_text)
        try:
            assert link.is_clickable(10) and link.is_visible(10)
            is_open = link.has_class('open')
            # do not click if tag group is already open
            if not is_open:
                link.click()
            return link
        except (WebDriverException, ElementClickInterceptedException, AssertionError):
            raise Exception("Could not click tab group link with text '{}'".format(link_text))


