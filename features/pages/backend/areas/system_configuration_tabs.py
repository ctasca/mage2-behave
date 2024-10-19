from stere.areas import Area
from stere.fields import Root
from features.core_config.backend.locators.system_configuration import *
from ..fields.system_configuration_tab import SystemConfigurationTab


class SystemConfigurationTabs(Area):
    GENERAL = 'general'
    CATALOG = 'catalog'
    SECURITY = 'security'
    CUSTOMERS = 'customers'
    SALES = 'sales'
    SERVICES = 'services'
    ADVANCED = 'advanced'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(TABS_ROOT_LOCATOR[STRATEGY_KEY], TABS_ROOT_LOCATOR[LOCATOR_KEY])
        self.general = SystemConfigurationTab(TAB_LOCATOR_FORMAT[STRATEGY_KEY],
                                              TAB_LOCATOR_FORMAT[LOCATOR_KEY].format('General'))
        self.catalog = SystemConfigurationTab(TAB_LOCATOR_FORMAT[STRATEGY_KEY],
                                              TAB_LOCATOR_FORMAT[LOCATOR_KEY].format('Catalog'))
        self.security = SystemConfigurationTab(TAB_LOCATOR_FORMAT[STRATEGY_KEY],
                                               TAB_LOCATOR_FORMAT[LOCATOR_KEY].format('Security'))
        self.customers = SystemConfigurationTab(TAB_LOCATOR_FORMAT[STRATEGY_KEY],
                                                TAB_LOCATOR_FORMAT[LOCATOR_KEY].format('Customers'))
        self.sales = SystemConfigurationTab(TAB_LOCATOR_FORMAT[STRATEGY_KEY],
                                            TAB_LOCATOR_FORMAT[LOCATOR_KEY].format('Sales'))
        self.services = SystemConfigurationTab(TAB_LOCATOR_FORMAT[STRATEGY_KEY],
                                               TAB_LOCATOR_FORMAT[LOCATOR_KEY].format('Services'))
        self.advanced = SystemConfigurationTab(TAB_LOCATOR_FORMAT[STRATEGY_KEY],
                                               TAB_LOCATOR_FORMAT[LOCATOR_KEY].format('Advanced'))

    def get_tab(self, tab: str):
        return getattr(self, tab)

    def click_tab(self, tab: str):
        tab_to_click = self.get_tab(tab)
        assert tab_to_click.is_clickable(10) and tab_to_click.is_visible(10)
        is_not_expanded = tab_to_click.find_by_xpath('../..').has_class('_hide')
        if is_not_expanded:
            tab_to_click.click()
