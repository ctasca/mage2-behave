from features.core_config.backend.locators.dashboard import *
from features.core_config.strategies import STRATEGY_KEY, LOCATOR_KEY
from stere.areas import Area
from ..fields.dashboard_store_stats_tabs import *


class DashboardStoreStats(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bestsellers_tab = BestsellersTab(DASHBOARD_BESTSELLERS_TAB_LOCATOR[STRATEGY_KEY],
                                              DASHBOARD_BESTSELLERS_TAB_LOCATOR[LOCATOR_KEY])
        self.most_viewed_products_tab = MostViewedProductsTab(DASHBOARD_REVIEWED_PRODUCTS_TAB_LOCATOR[STRATEGY_KEY],
                                                              DASHBOARD_REVIEWED_PRODUCTS_TAB_LOCATOR[LOCATOR_KEY])
        self.new_customers_tab = NewCustomersTab(DASHBOARD_NEW_CUSTOMERS_TAB_LOCATOR[STRATEGY_KEY],
                                                 DASHBOARD_NEW_CUSTOMERS_TAB_LOCATOR[LOCATOR_KEY])
        self.customers_tab = CustomersTab(DASHBOARD_CUSTOMERS_TAB_LOCATOR[STRATEGY_KEY],
                                          DASHBOARD_CUSTOMERS_TAB_LOCATOR[LOCATOR_KEY])
