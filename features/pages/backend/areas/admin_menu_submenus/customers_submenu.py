import features.core_config.backend.backend_locators as bl
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.customers_submenu_links import *
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
from typing import List


class CustomersSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.ADMIN_MENU_ROOT[STRATEGY_KEY], bl.ADMIN_MENU_ROOT[LOCATOR_KEY])
        self.all_customers = AllCustomers(bl.CUSTOMERS_SUBMENU_ALL_CUSTOMERS_LINK_LOCATOR[STRATEGY_KEY],
                                          bl.CUSTOMERS_SUBMENU_ALL_CUSTOMERS_LINK_LOCATOR[LOCATOR_KEY])
        self.now_online = NowOnline(bl.CUSTOMERS_SUBMENU_ONLINE_LINK_LOCATOR[STRATEGY_KEY],
                                    bl.CUSTOMERS_SUBMENU_ONLINE_LINK_LOCATOR[LOCATOR_KEY])
        self.login_as_customer_log = LoginAsCustomerLog(bl.CUSTOMERS_SUBMENU_AS_CUSTOMER_LOG_LINK_LOCATOR[STRATEGY_KEY],
                                                        bl.CUSTOMERS_SUBMENU_AS_CUSTOMER_LOG_LINK_LOCATOR[LOCATOR_KEY])
        self.customer_groups = CustomerGroups(bl.CUSTOMERS_SUBMENU_GROUPS_LINK_LOCATOR[STRATEGY_KEY],
                                              bl.CUSTOMERS_SUBMENU_GROUPS_LINK_LOCATOR[LOCATOR_KEY])

    def links(self) -> List[Link]:
        return [
            self.all_customers,
            self.now_online,
            self.login_as_customer_log,
            self.customer_groups
        ]
