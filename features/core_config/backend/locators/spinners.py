from typing import Dict

from features.core_config.strategies import STRATEGY_KEY, XPATH_STRATEGY, LOCATOR_KEY

SPINNER_DATA_ROLE_LOCATOR: Dict[str, str] = {STRATEGY_KEY: XPATH_STRATEGY,
                                             LOCATOR_KEY: "//div[@data-role='spinner']"}
