from typing import Dict

from features.core_config.strategies import STRATEGY_KEY, XPATH_STRATEGY, LOCATOR_KEY

ORDERS_PURCHASE_DATE_FROM_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"created_at[from]\"]"}
ORDERS_PURCHASE_DATE_TO_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"created_at[to]\"]"}
ORDERS_BASE_GRAND_TOTAL_FROM_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"base_grand_total[from]\"]"}
ORDERS_BASE_GRAND_TOTAL_TO_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"base_grand_total[to]\"]"}
ORDERS_PURCHASED_GRAND_TOTAL_FROM_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"grand_total[from]\"]"}
ORDERS_PURCHASED_GRAND_TOTAL_TO_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"grand_total[to]\"]"}
ORDERS_PURCHASE_POINT_SELECT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//select[@name=\"store_id\"]"}
