from typing import Dict

from features.core_config.strategies import STRATEGY_KEY, XPATH_STRATEGY, LOCATOR_KEY, ID_STRATEGY

DASHBOARD_RELOAD_DATA_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//button[@title=\"Reload Data\"]"}
DASHBOARD_DIAGRAM_ORDER_TAB_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "diagram_tab_orders"}
DASHBOARD_DIAGRAM_AMOUNTS_TAB_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "diagram_tab_amounts"}
DASHBOARD_BESTSELLERS_TAB_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "grid_tab_ordered_products"}
DASHBOARD_REVIEWED_PRODUCTS_TAB_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "grid_tab_reviewed_products"}
DASHBOARD_NEW_CUSTOMERS_TAB_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "grid_tab_new_customers"}
DASHBOARD_CUSTOMERS_TAB_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "grid_tab_customers"}
