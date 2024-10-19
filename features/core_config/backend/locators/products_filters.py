from typing import Dict

from features.core_config.strategies import STRATEGY_KEY, XPATH_STRATEGY, LOCATOR_KEY

PRODUCTS_FROM_ID_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"entity_id[from]\"]"}
PRODUCTS_TO_ID_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"entity_id[to]\"]"}
PRODUCTS_FROM_PRICE_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"price[from]\"]"}
PRODUCTS_TO_PRICE_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"price[to]\"]"}
PRODUCTS_FROM_QTY_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"qty[from]\"]"}
PRODUCTS_TO_QTY_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"qty[to]\"]"}
PRODUCTS_FROM_LAST_UPDATED_AT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"updated_at[from]\"]"}
PRODUCTS_TO_LAST_UPDATED_AT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"updated_at[to]\"]"}
PRODUCTS_STORE_VIEW_SELECT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//select[@name=\"store_id\"]"}
PRODUCTS_ASSET_SELECT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//div[@data-role='advanced-select']"}
PRODUCTS_ASSET_SELECT_TEXT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@data-role='advanced-select-text']"}
PRODUCTS_ASSET_SELECT_OPTION_FILTER_LOCATOR_FORMAT: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY,
     LOCATOR_KEY: "//label[contains(@class, 'admin__action-multiselect-label')]//span[contains(text(), '{}')]"}
PRODUCTS_ASSET_SELECT_FILTER_ITEMS_QUANTITY_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//div[@data-bind='text: itemsQuantity']"}
PRODUCTS_ASSET_DONE_BUTTON_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//button[@data-action='close-advanced-select']"}
PRODUCTS_NAME_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"name\"]"}
PRODUCTS_TYPE_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//select[@name=\"type_id\"]"}
PRODUCTS_ATTRIBUTE_SET_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//select[@name=\"attribute_set_id\"]"}
PRODUCTS_SKU_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"sku\"]"}
PRODUCTS_VISIBILITY_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//select[@name=\"visibility\"]"}
PRODUCTS_STATUS_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//select[@name=\"status\"]"}
