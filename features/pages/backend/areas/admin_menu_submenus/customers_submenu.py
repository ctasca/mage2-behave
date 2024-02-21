import features.core_config.all as config
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.customers_submenu_links import *


class CustomersSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(config.ADMIN_MENU_ROOT['strategy'], config.ADMIN_MENU_ROOT['locator'])
        self.all_customers = AllCustomers(config.CUSTOMERS_SUBMENU_ALL_CUSTOMERS_LINK_LOCATOR['strategy'],
                                          config.CUSTOMERS_SUBMENU_ALL_CUSTOMERS_LINK_LOCATOR['locator'])
        self.now_online = NowOnline(config.CUSTOMERS_SUBMENU_ONLINE_LINK_LOCATOR['strategy'],
                                    config.CUSTOMERS_SUBMENU_ONLINE_LINK_LOCATOR['locator'])
        self.login_as_customer_log = LoginAsCustomerLog(
            config.CUSTOMERS_SUBMENU_AS_CUSTOMER_LOG_LINK_LOCATOR['strategy'],
            config.CUSTOMERS_SUBMENU_AS_CUSTOMER_LOG_LINK_LOCATOR['locator'])
        self.customer_groups = CustomerGroups(config.CUSTOMERS_SUBMENU_GROUPS_LINK_LOCATOR['strategy'],
                                              config.CUSTOMERS_SUBMENU_GROUPS_LINK_LOCATOR['locator'])
