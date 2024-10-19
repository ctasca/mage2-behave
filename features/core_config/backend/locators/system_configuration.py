from typing import Dict

from features.core_config.strategies import STRATEGY_KEY, XPATH_STRATEGY, ID_STRATEGY, LOCATOR_KEY

TABS_ROOT_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: 'system_config_tabs'}
TAB_LOCATOR_FORMAT: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//div[@id='system_config_tabs']//strong[text()='{}']"}
TAB_LINK_LOCATOR_FORMAT: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//a[@class='admin__page-nav-link item-nav']//span[text()='{}']"}
TAB_GROUP_LINK_LOCATOR_FORMAT: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//form[@id='config-edit-form']//a[text()='{}']"}
SAVE_BUTTON_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "save"}
