import core_config.all as config
from stere.areas import Area
from pages.backend.fields.catalog_submenu_links import *

class CatalogSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products = Products(config.CATALOG_SUBMENU_PRODUCTS_LINK_LOCATOR['strategy'], config.CATALOG_SUBMENU_PRODUCTS_LINK_LOCATOR['locator'])
        self.categories = Categories(config.CATALOG_SUBMENU_CATEGORIES_LINK_LOCATOR['strategy'], config.CATALOG_SUBMENU_CATEGORIES_LINK_LOCATOR['locator'])