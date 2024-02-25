from features.core_config.backend.backend_locators import *
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.catalog_submenu_links import Products, Categories


class CatalogSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(ADMIN_MENU_ROOT['strategy'], ADMIN_MENU_ROOT['locator'])
        self.products = Products(CATALOG_SUBMENU_PRODUCTS_LINK_LOCATOR['strategy'],
                                 CATALOG_SUBMENU_PRODUCTS_LINK_LOCATOR['locator'])
        self.categories = Categories(CATALOG_SUBMENU_CATEGORIES_LINK_LOCATOR['strategy'],
                                     CATALOG_SUBMENU_CATEGORIES_LINK_LOCATOR['locator'])
