from stere.areas import Area
from stere.fields import Link, Root
from typing import List
from features.pages.backend.fields.submenu_link import SubmenuLink
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
import features.core_config.backend.backend_locators as bl


class CatalogSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.ADMIN_MENU_ROOT[STRATEGY_KEY], bl.ADMIN_MENU_ROOT[LOCATOR_KEY])
        self.products = SubmenuLink(bl.CATALOG_SUBMENU_PRODUCTS_LINK_LOCATOR[STRATEGY_KEY],
                                 bl.CATALOG_SUBMENU_PRODUCTS_LINK_LOCATOR[LOCATOR_KEY])
        self.categories = SubmenuLink(bl.CATALOG_SUBMENU_CATEGORIES_LINK_LOCATOR[STRATEGY_KEY],
                                     bl.CATALOG_SUBMENU_CATEGORIES_LINK_LOCATOR[LOCATOR_KEY])

    def links(self) -> List[Link]:
        return [
            self.products,
            self.categories
        ]
