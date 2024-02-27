import features.core_config.backend.backend_locators as bl
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.stores_submenu_links import *
from typing import List


class StoresSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.ADMIN_MENU_ROOT['strategy'], bl.ADMIN_MENU_ROOT['locator'])
        self.all_stores = AllStores(bl.STORES_SUBMENU_ALL_STORES_LINK_LOCATOR['strategy'],
                                    bl.STORES_SUBMENU_ALL_STORES_LINK_LOCATOR['locator'])
        self.configuration = Configuration(bl.STORES_SUBMENU_CONFIGURATION_LINK_LOCATOR['strategy'],
                                           bl.STORES_SUBMENU_CONFIGURATION_LINK_LOCATOR['locator'])
        self.terms_and_conditions = TermsAndConditions(
            bl.STORES_SUBMENU_TERMS_AND_CONDITIONS_LINK_LOCATOR['strategy'],
            bl.STORES_SUBMENU_TERMS_AND_CONDITIONS_LINK_LOCATOR['locator'])
        self.order_status = OrderStatus(bl.STORES_SUBMENU_ORDER_STATUS_LINK_LOCATOR['strategy'],
                                        bl.STORES_SUBMENU_ORDER_STATUS_LINK_LOCATOR['locator'])
        self.sources = Sources(bl.STORES_SUBMENU_SOURCES_LINK_LOCATOR['strategy'],
                               bl.STORES_SUBMENU_SOURCES_LINK_LOCATOR['locator'])
        self.stocks = Stocks(bl.STORES_SUBMENU_STOCKS_LINK_LOCATOR['strategy'],
                             bl.STORES_SUBMENU_STOCKS_LINK_LOCATOR['locator'])
        self.tax_rules = TaxRules(bl.STORES_SUBMENU_TAX_RULES_LINK_LOCATOR['strategy'],
                                  bl.STORES_SUBMENU_TAX_RULES_LINK_LOCATOR['locator'])
        self.tax_zones_and_rates = TaxZonesAndRates(bl.STORES_SUBMENU_TAX_ZONES_AND_RATES_LINK_LOCATOR['strategy'],
                                                    bl.STORES_SUBMENU_TAX_ZONES_AND_RATES_LINK_LOCATOR['locator'])
        self.currency_rates = CurrencyRates(bl.STORES_SUBMENU_CURRENCY_RATES_LINK_LOCATOR['strategy'],
                                            bl.STORES_SUBMENU_CURRENCY_RATES_LINK_LOCATOR['locator'])
        self.currency_symbols = CurrencySymbols(bl.STORES_SUBMENU_CURRENCY_SYMBOLS_LINK_LOCATOR['strategy'],
                                                bl.STORES_SUBMENU_CURRENCY_SYMBOLS_LINK_LOCATOR['locator'])
        self.product = Product(bl.STORES_SUBMENU_PRODUCT_LINK_LOCATOR['strategy'],
                               bl.STORES_SUBMENU_PRODUCT_LINK_LOCATOR['locator'])
        self.attribute_set = AttributeSet(bl.STORES_SUBMENU_ATTRIBUTE_SET_LINK_LOCATOR['strategy'],
                                          bl.STORES_SUBMENU_ATTRIBUTE_SET_LINK_LOCATOR['locator'])
        self.rating = Rating(bl.STORES_SUBMENU_RATING_LINK_LOCATOR['strategy'],
                             bl.STORES_SUBMENU_RATING_LINK_LOCATOR['locator'])

    def links(self) -> List[Link]:
        return [
            self.all_stores,
            self.configuration,
            self.terms_and_conditions,
            self.order_status,
            self.sources,
            self.stocks,
            self.tax_rules,
            self.tax_zones_and_rates,
            self.currency_rates,
            self.currency_symbols,
            self.product,
            self.attribute_set,
            self.rating
        ]
