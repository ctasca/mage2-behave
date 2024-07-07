from typing import Dict

from features.core_config.strategies import STRATEGY_KEY, XPATH_STRATEGY, LOCATOR_KEY

CACHE_TYPE_LOCATOR_FORMAT: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//td[@data-column='cache_type' and normalize-space(text())='{}']"}
CACHE_TYPE_CHECKBOX_LOCATOR_FORMAT: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "{}/preceding-sibling::td//label//label".format(
        CACHE_TYPE_LOCATOR_FORMAT[LOCATOR_KEY]
    )}
