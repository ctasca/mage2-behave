import features.core_config.all as config
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.catalog_submenu_links import Products, Categories


class CatalogSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(config.ADMIN_MENU_ROOT['strategy'], config.ADMIN_MENU_ROOT['locator'])
        self.products = Products(config.CATALOG_SUBMENU_PRODUCTS_LINK_LOCATOR['strategy'],
                                 config.CATALOG_SUBMENU_PRODUCTS_LINK_LOCATOR['locator'])
        self.categories = Categories(config.CATALOG_SUBMENU_CATEGORIES_LINK_LOCATOR['strategy'],
                                     config.CATALOG_SUBMENU_CATEGORIES_LINK_LOCATOR['locator'])
