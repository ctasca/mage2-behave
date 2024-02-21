import core_config.all as config
from stere.areas import Area
from stere.fields import Root
from pages.backend.fields.stores_submenu_links import *

class StoresSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(config.ADMIN_MENU_ROOT['strategy'], config.ADMIN_MENU_ROOT['locator'])
        self.all_stores = AllStores(config.STORES_SUBMENU_ALL_STORES_LINK_LOCATOR['strategy'], config.STORES_SUBMENU_ALL_STORES_LINK_LOCATOR['locator'])
        self.configuration = Configuration(config.STORES_SUBMENU_CONFIGURATION_LINK_LOCATOR['strategy'], config.STORES_SUBMENU_CONFIGURATION_LINK_LOCATOR['locator'])
        self.terms_and_conditions = TermsAndConditions(config.STORES_SUBMENU_TERMS_AND_CONDITIONS_LINK_LOCATOR['strategy'], config.STORES_SUBMENU_TERMS_AND_CONDITIONS_LINK_LOCATOR['locator'])
        self.order_status = OrderStatus(config.STORES_SUBMENU_ORDER_STATUS_LINK_LOCATOR['strategy'], config.STORES_SUBMENU_ORDER_STATUS_LINK_LOCATOR['locator'])
        self.sources = Sources(config.STORES_SUBMENU_SOURCES_LINK_LOCATOR['strategy'], config.STORES_SUBMENU_SOURCES_LINK_LOCATOR['locator'])
        self.stocks = Stocks(config.STORES_SUBMENU_STOCKS_LINK_LOCATOR['strategy'], config.STORES_SUBMENU_STOCKS_LINK_LOCATOR['locator'])
        self.tax_rules = TaxRules(config.STORES_SUBMENU_TAX_RULES_LINK_LOCATOR['strategy'], config.STORES_SUBMENU_TAX_RULES_LINK_LOCATOR['locator'])
        self.tax_zones_and_rates = TaxZonesAndRates(config.STORES_SUBMENU_TAX_ZONES_AND_RATES_LINK_LOCATOR['strategy'], config.STORES_SUBMENU_TAX_ZONES_AND_RATES_LINK_LOCATOR['locator'])
        self.currency_rates = CurrencyRates(config.STORES_SUBMENU_CURRENCY_RATES_LINK_LOCATOR['strategy'], config.STORES_SUBMENU_CURRENCY_RATES_LINK_LOCATOR['locator'])
        self.currency_symbols = CurrencySymbols(config.STORES_SUBMENU_CURRENCY_SYMBOLS_LINK_LOCATOR['strategy'], config.STORES_SUBMENU_CURRENCY_SYMBOLS_LINK_LOCATOR['locator'])
        self.product = Product(config.STORES_SUBMENU_PRODUCT_LINK_LOCATOR['strategy'], config.STORES_SUBMENU_PRODUCT_LINK_LOCATOR['locator'])
        self.attribute_set = AttributeSet(config.STORES_SUBMENU_ATTRIBUTE_SET_LINK_LOCATOR['strategy'], config.STORES_SUBMENU_ATTRIBUTE_SET_LINK_LOCATOR['locator'])
        self.rating = Rating(config.STORES_SUBMENU_RATING_LINK_LOCATOR['strategy'], config.STORES_SUBMENU_RATING_LINK_LOCATOR['locator'])