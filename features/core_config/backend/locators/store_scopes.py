from typing import Dict

from features.core_config.strategies import STRATEGY_KEY, ID_STRATEGY, LOCATOR_KEY, XPATH_STRATEGY

STORE_CHANGE_BUTTON_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "store-change-button"}
STORE_SCOPE_LIST_ROOT_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//ul[@data-role='stores-list']"}
SET_STORE_SCOPE_LOCATOR_FORMAT: str = "//a[contains(text(), '{}')]"
