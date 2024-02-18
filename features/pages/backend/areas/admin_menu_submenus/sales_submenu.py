import core_config.all as config
from stere.areas import Area
from pages.backend.fields.sales_submenu_links import *

class SalesSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orders = Orders(config.SALES_SUBMENU_ORDERS_LINK_LOCATOR['strategy'], config.SALES_SUBMENU_ORDERS_LINK_LOCATOR['locator'])
        self.invoices = Invoices(config.SALES_SUBMENU_INVOICES_LINK_LOCATOR['strategy'], config.SALES_SUBMENU_INVOICES_LINK_LOCATOR['locator'])
        self.shipments = Shipments(config.SALES_SUBMENU_SHIPMENTS_LINK_LOCATOR['strategy'], config.SALES_SUBMENU_SHIPMENTS_LINK_LOCATOR['locator'])
        self.creditmemos = CreditMemos(config.SALES_SUBMENU_CREDITMEMOS_LINK_LOCATOR['strategy'], config.SALES_SUBMENU_CREDITMEMOS_LINK_LOCATOR['locator'])
        self.billing_agreements = BillingAgreements(config.SALES_SUBMENU_BILLING_AGREEMENTS_LINK_LOCATOR['strategy'], config.SALES_SUBMENU_BILLING_AGREEMENTS_LINK_LOCATOR['locator'])
        self.transactions = Transactions(config.SALES_SUBMENU_TRANSACTIONS_LINK_LOCATOR['strategy'], config.SALES_SUBMENU_TRANSACTIONS_LINK_LOCATOR['locator'])
        self.virtual_terminal = BraintreeVirualTerminal(config.SALES_SUBMENU_VIRTUAL_TERMINAL_LINK_LOCATOR['strategy'], config.SALES_SUBMENU_VIRTUAL_TERMINAL_LINK_LOCATOR['locator'])