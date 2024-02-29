import features.core_config.backend.backend_locators as bl
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
from stere.areas import Area
from stere.fields import Root, Link
from features.pages.backend.fields.submenu_link import SubmenuLink
from typing import List


class SalesSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.ADMIN_MENU_ROOT[STRATEGY_KEY], bl.ADMIN_MENU_ROOT[LOCATOR_KEY])
        self.orders = SubmenuLink(bl.SALES_SUBMENU_ORDERS_LINK_LOCATOR[STRATEGY_KEY],
                                  bl.SALES_SUBMENU_ORDERS_LINK_LOCATOR[LOCATOR_KEY])
        self.invoices = SubmenuLink(bl.SALES_SUBMENU_INVOICES_LINK_LOCATOR[STRATEGY_KEY],
                                    bl.SALES_SUBMENU_INVOICES_LINK_LOCATOR[LOCATOR_KEY])
        self.shipments = SubmenuLink(bl.SALES_SUBMENU_SHIPMENTS_LINK_LOCATOR[STRATEGY_KEY],
                                     bl.SALES_SUBMENU_SHIPMENTS_LINK_LOCATOR[LOCATOR_KEY])
        self.creditmemos = SubmenuLink(bl.SALES_SUBMENU_CREDITMEMOS_LINK_LOCATOR[STRATEGY_KEY],
                                       bl.SALES_SUBMENU_CREDITMEMOS_LINK_LOCATOR[LOCATOR_KEY])
        self.billing_agreements = SubmenuLink(bl.SALES_SUBMENU_BILLING_AGREEMENTS_LINK_LOCATOR[STRATEGY_KEY],
                                              bl.SALES_SUBMENU_BILLING_AGREEMENTS_LINK_LOCATOR[LOCATOR_KEY])
        self.transactions = SubmenuLink(bl.SALES_SUBMENU_TRANSACTIONS_LINK_LOCATOR[STRATEGY_KEY],
                                        bl.SALES_SUBMENU_TRANSACTIONS_LINK_LOCATOR[LOCATOR_KEY])
        self.virtual_terminal = SubmenuLink(bl.SALES_SUBMENU_VIRTUAL_TERMINAL_LINK_LOCATOR[STRATEGY_KEY],
                                            bl.SALES_SUBMENU_VIRTUAL_TERMINAL_LINK_LOCATOR[LOCATOR_KEY])

    def links(self) -> List[Link]:
        return [
            self.orders,
            self.invoices,
            self.shipments,
            self.creditmemos,
            self.billing_agreements,
            self.transactions,
            self.virtual_terminal
        ]
