import features.core_config.backend.backend_locators as bl
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
from stere.areas import Area
from stere.fields import Root, Link
from features.pages.backend.fields.submenu_link import SubmenuLink
from typing import List


class StoresSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.ADMIN_MENU_ROOT[STRATEGY_KEY], bl.ADMIN_MENU_ROOT[LOCATOR_KEY])
        self.all_stores = SubmenuLink(bl.STORES_SUBMENU_ALL_STORES_LINK_LOCATOR[STRATEGY_KEY],
                                      bl.STORES_SUBMENU_ALL_STORES_LINK_LOCATOR[LOCATOR_KEY])
        self.configuration = SubmenuLink(bl.STORES_SUBMENU_CONFIGURATION_LINK_LOCATOR[STRATEGY_KEY],
                                         bl.STORES_SUBMENU_CONFIGURATION_LINK_LOCATOR[LOCATOR_KEY])
        self.terms_and_conditions = SubmenuLink(
            bl.STORES_SUBMENU_TERMS_AND_CONDITIONS_LINK_LOCATOR[STRATEGY_KEY],
            bl.STORES_SUBMENU_TERMS_AND_CONDITIONS_LINK_LOCATOR[LOCATOR_KEY])
        self.order_status = SubmenuLink(bl.STORES_SUBMENU_ORDER_STATUS_LINK_LOCATOR[STRATEGY_KEY],
                                        bl.STORES_SUBMENU_ORDER_STATUS_LINK_LOCATOR[LOCATOR_KEY])
        self.sources = SubmenuLink(bl.STORES_SUBMENU_SOURCES_LINK_LOCATOR[STRATEGY_KEY],
                                   bl.STORES_SUBMENU_SOURCES_LINK_LOCATOR[LOCATOR_KEY])
        self.stocks = SubmenuLink(bl.STORES_SUBMENU_STOCKS_LINK_LOCATOR[STRATEGY_KEY],
                                  bl.STORES_SUBMENU_STOCKS_LINK_LOCATOR[LOCATOR_KEY])
        self.tax_rules = SubmenuLink(bl.STORES_SUBMENU_TAX_RULES_LINK_LOCATOR[STRATEGY_KEY],
                                     bl.STORES_SUBMENU_TAX_RULES_LINK_LOCATOR[LOCATOR_KEY])
        self.tax_zones_and_rates = SubmenuLink(bl.STORES_SUBMENU_TAX_ZONES_AND_RATES_LINK_LOCATOR[STRATEGY_KEY],
                                               bl.STORES_SUBMENU_TAX_ZONES_AND_RATES_LINK_LOCATOR[LOCATOR_KEY])
        self.currency_rates = SubmenuLink(bl.STORES_SUBMENU_CURRENCY_RATES_LINK_LOCATOR[STRATEGY_KEY],
                                          bl.STORES_SUBMENU_CURRENCY_RATES_LINK_LOCATOR[LOCATOR_KEY])
        self.currency_symbols = SubmenuLink(bl.STORES_SUBMENU_CURRENCY_SYMBOLS_LINK_LOCATOR[STRATEGY_KEY],
                                            bl.STORES_SUBMENU_CURRENCY_SYMBOLS_LINK_LOCATOR[LOCATOR_KEY])
        self.product = SubmenuLink(bl.STORES_SUBMENU_PRODUCT_LINK_LOCATOR[STRATEGY_KEY],
                                   bl.STORES_SUBMENU_PRODUCT_LINK_LOCATOR[LOCATOR_KEY])
        self.attribute_set = SubmenuLink(bl.STORES_SUBMENU_ATTRIBUTE_SET_LINK_LOCATOR[STRATEGY_KEY],
                                         bl.STORES_SUBMENU_ATTRIBUTE_SET_LINK_LOCATOR[LOCATOR_KEY])
        self.rating = SubmenuLink(bl.STORES_SUBMENU_RATING_LINK_LOCATOR[STRATEGY_KEY],
                                  bl.STORES_SUBMENU_RATING_LINK_LOCATOR[LOCATOR_KEY])

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
