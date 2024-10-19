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
ORDERS_INCREMENT_ID_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"increment_id\"]"}
ORDERS_BILL_TO_NAME_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"billing_name\"]"}
ORDERS_SHIP_TO_NAME_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"shipping_name\"]"}
ORDERS_STATUS_SELECT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//select[@name=\"status\"]"}
ORDERS_BRAINTREE_TRANSACTION_SOURCE_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"transaction_source\"]"}
