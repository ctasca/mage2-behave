from features.core_config.backend.locators.admin_menu import ADMIN_MENU_ROOT
from features.core_config.backend.locators.admin_submenus import *
from stere.areas import Area
from stere.fields import Link, Root
from typing import List
from features.pages.backend.fields.submenu_link import SubmenuLink
from features.core_config.strategies import STRATEGY_KEY, LOCATOR_KEY


class CatalogSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(ADMIN_MENU_ROOT[STRATEGY_KEY], ADMIN_MENU_ROOT[LOCATOR_KEY])
        self.products = SubmenuLink(CATALOG_SUBMENU_PRODUCTS_LINK_LOCATOR[STRATEGY_KEY],
                                    CATALOG_SUBMENU_PRODUCTS_LINK_LOCATOR[LOCATOR_KEY])
        self.categories = SubmenuLink(CATALOG_SUBMENU_CATEGORIES_LINK_LOCATOR[STRATEGY_KEY],
                                      CATALOG_SUBMENU_CATEGORIES_LINK_LOCATOR[LOCATOR_KEY])

    def links(self) -> List[Link]:
        return [
            self.products,
            self.categories
        ]
