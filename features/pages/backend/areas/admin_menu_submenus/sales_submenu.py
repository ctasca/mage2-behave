import features.core_config.backend.backend_locators as bl
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.sales_submenu_links import *
from typing import List


class SalesSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.ADMIN_MENU_ROOT['strategy'], bl.ADMIN_MENU_ROOT['locator'])
        self.orders = Orders(bl.SALES_SUBMENU_ORDERS_LINK_LOCATOR['strategy'],
                             bl.SALES_SUBMENU_ORDERS_LINK_LOCATOR['locator'])
        self.invoices = Invoices(bl.SALES_SUBMENU_INVOICES_LINK_LOCATOR['strategy'],
                                 bl.SALES_SUBMENU_INVOICES_LINK_LOCATOR['locator'])
        self.shipments = Shipments(bl.SALES_SUBMENU_SHIPMENTS_LINK_LOCATOR['strategy'],
                                   bl.SALES_SUBMENU_SHIPMENTS_LINK_LOCATOR['locator'])
        self.creditmemos = CreditMemos(bl.SALES_SUBMENU_CREDITMEMOS_LINK_LOCATOR['strategy'],
                                       bl.SALES_SUBMENU_CREDITMEMOS_LINK_LOCATOR['locator'])
        self.billing_agreements = BillingAgreements(bl.SALES_SUBMENU_BILLING_AGREEMENTS_LINK_LOCATOR['strategy'],
                                                    bl.SALES_SUBMENU_BILLING_AGREEMENTS_LINK_LOCATOR['locator'])
        self.transactions = Transactions(bl.SALES_SUBMENU_TRANSACTIONS_LINK_LOCATOR['strategy'],
                                         bl.SALES_SUBMENU_TRANSACTIONS_LINK_LOCATOR['locator'])
        self.virtual_terminal = BraintreeVirualTerminal(bl.SALES_SUBMENU_VIRTUAL_TERMINAL_LINK_LOCATOR['strategy'],
                                                        bl.SALES_SUBMENU_VIRTUAL_TERMINAL_LINK_LOCATOR['locator'])

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
