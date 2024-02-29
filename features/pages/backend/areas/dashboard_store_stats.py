import features.core_config.backend.backend_locators as bl
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
from stere.areas import Area
from ..fields.dashboard_store_stats_tabs import *


class DashboardStoreStats(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bestsellers_tab = BestsellersTab(bl.DASHBOARD_BESTSELLERS_TAB_LOCATOR[STRATEGY_KEY],
                                              bl.DASHBOARD_BESTSELLERS_TAB_LOCATOR[LOCATOR_KEY])
        self.most_viewed_products_tab = MostViewedProductsTab(bl.DASHBOARD_REVIEWED_PRODUCTS_TAB_LOCATOR[STRATEGY_KEY],
                                                              bl.DASHBOARD_REVIEWED_PRODUCTS_TAB_LOCATOR[LOCATOR_KEY])
        self.new_customers_tab = NewCustomersTab(bl.DASHBOARD_NEW_CUSTOMERS_TAB_LOCATOR[STRATEGY_KEY],
                                                 bl.DASHBOARD_NEW_CUSTOMERS_TAB_LOCATOR[LOCATOR_KEY])
        self.customers_tab = CustomersTab(bl.DASHBOARD_CUSTOMERS_TAB_LOCATOR[STRATEGY_KEY],
                                          bl.DASHBOARD_CUSTOMERS_TAB_LOCATOR[LOCATOR_KEY])
