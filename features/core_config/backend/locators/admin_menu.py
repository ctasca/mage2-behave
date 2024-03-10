from typing import Dict

from features.core_config.strategies import STRATEGY_KEY, ID_STRATEGY, LOCATOR_KEY

ADMIN_MENU_ROOT: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "nav"}
ADMIN_MENU_DASHBOARD_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-backend-dashboard"}
ADMIN_MENU_SALES_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-sales-sales"}
ADMIN_MENU_CATALOG_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-catalog-catalog"}
ADMIN_MENU_CUSTOMERS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-customer-customer"}
ADMIN_MENU_MARKETING_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-backend-marketing"}
ADMIN_MENU_CONTENT_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-backend-content"}
ADMIN_MENU_REPORTS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-reports-report"}
ADMIN_MENU_STORES_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-backend-stores"}
ADMIN_MENU_SYSTEM_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-backend-system"}
