from features.core_config.backend.backend_locators import *
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.customers_submenu_links import *
from typing import List


class CustomersSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(ADMIN_MENU_ROOT['strategy'], ADMIN_MENU_ROOT['locator'])
        self.all_customers = AllCustomers(CUSTOMERS_SUBMENU_ALL_CUSTOMERS_LINK_LOCATOR['strategy'],
                                          CUSTOMERS_SUBMENU_ALL_CUSTOMERS_LINK_LOCATOR['locator'])
        self.now_online = NowOnline(CUSTOMERS_SUBMENU_ONLINE_LINK_LOCATOR['strategy'],
                                    CUSTOMERS_SUBMENU_ONLINE_LINK_LOCATOR['locator'])
        self.login_as_customer_log = LoginAsCustomerLog(
            CUSTOMERS_SUBMENU_AS_CUSTOMER_LOG_LINK_LOCATOR['strategy'],
            CUSTOMERS_SUBMENU_AS_CUSTOMER_LOG_LINK_LOCATOR['locator'])
        self.customer_groups = CustomerGroups(CUSTOMERS_SUBMENU_GROUPS_LINK_LOCATOR['strategy'],
                                              CUSTOMERS_SUBMENU_GROUPS_LINK_LOCATOR['locator'])

    def links(self) -> List[Link]:
        return [
            self.all_customers,
            self.now_online,
            self.login_as_customer_log,
            self.customer_groups
        ]
