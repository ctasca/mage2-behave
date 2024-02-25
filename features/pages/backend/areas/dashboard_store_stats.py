from features.core_config.backend.backend_locators import *
from stere.areas import Area
from ..fields.dashboard_store_stats_tabs import *


class DashboardStoreStats(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bestsellers_tab = BestsellersTab(DASHBOARD_BESTSELLERS_TAB_LOCATOR['strategy'],
                                              DASHBOARD_BESTSELLERS_TAB_LOCATOR['locator'])
        self.most_viewed_products_tab = MostViewedProductsTab(DASHBOARD_REVIEWED_PRODUCTS_TAB_LOCATOR['strategy'],
                                                              DASHBOARD_REVIEWED_PRODUCTS_TAB_LOCATOR['locator'])
        self.new_customers_tab = NewCustomersTab(DASHBOARD_NEW_CUSTOMERS_TAB_LOCATOR['strategy'],
                                                 DASHBOARD_NEW_CUSTOMERS_TAB_LOCATOR['locator'])
        self.customers_tab = CustomersTab(DASHBOARD_CUSTOMERS_TAB_LOCATOR['strategy'],
                                          DASHBOARD_CUSTOMERS_TAB_LOCATOR['locator'])
