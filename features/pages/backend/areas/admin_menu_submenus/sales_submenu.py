from features.core_config.backend.backend_locators import *
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.sales_submenu_links import *


class SalesSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(ADMIN_MENU_ROOT['strategy'], ADMIN_MENU_ROOT['locator'])
        self.orders = Orders(SALES_SUBMENU_ORDERS_LINK_LOCATOR['strategy'],
                             SALES_SUBMENU_ORDERS_LINK_LOCATOR['locator'])
        self.invoices = Invoices(SALES_SUBMENU_INVOICES_LINK_LOCATOR['strategy'],
                                 SALES_SUBMENU_INVOICES_LINK_LOCATOR['locator'])
        self.shipments = Shipments(SALES_SUBMENU_SHIPMENTS_LINK_LOCATOR['strategy'],
                                   SALES_SUBMENU_SHIPMENTS_LINK_LOCATOR['locator'])
        self.creditmemos = CreditMemos(SALES_SUBMENU_CREDITMEMOS_LINK_LOCATOR['strategy'],
                                       SALES_SUBMENU_CREDITMEMOS_LINK_LOCATOR['locator'])
        self.billing_agreements = BillingAgreements(SALES_SUBMENU_BILLING_AGREEMENTS_LINK_LOCATOR['strategy'],
                                                    SALES_SUBMENU_BILLING_AGREEMENTS_LINK_LOCATOR['locator'])
        self.transactions = Transactions(SALES_SUBMENU_TRANSACTIONS_LINK_LOCATOR['strategy'],
                                         SALES_SUBMENU_TRANSACTIONS_LINK_LOCATOR['locator'])
        self.virtual_terminal = BraintreeVirualTerminal(SALES_SUBMENU_VIRTUAL_TERMINAL_LINK_LOCATOR['strategy'],
                                                        SALES_SUBMENU_VIRTUAL_TERMINAL_LINK_LOCATOR['locator'])
