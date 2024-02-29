from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
import features.core_config.backend.backend_locators as bl
from stere.fields import Link
from stere.areas import Area
from .admin_menu_submenus.sales_submenu import SalesSubmenu
from .admin_menu_submenus.catalog_submenu import CatalogSubmenu
from .admin_menu_submenus.customers_submenu import CustomersSubmenu
from .admin_menu_submenus.marketing_submenu import MarketingSubmenu
from .admin_menu_submenus.content_submenu import ContentSubmenu
from .admin_menu_submenus.reports_submenu import ReportsSubmenu
from .admin_menu_submenus.stores_submenu import StoresSubmenu
from .admin_menu_submenus.system_submenu import SystemSubmenu


class AdminMenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dashboard = Link(bl.ADMIN_MENU_DASHBOARD_LINK_LOCATOR[STRATEGY_KEY],
                              bl.ADMIN_MENU_DASHBOARD_LINK_LOCATOR[LOCATOR_KEY])
        self.sales = Link(bl.ADMIN_MENU_SALES_LINK_LOCATOR[STRATEGY_KEY],
                          bl.ADMIN_MENU_SALES_LINK_LOCATOR[LOCATOR_KEY])
        self.catalog = Link(bl.ADMIN_MENU_CATALOG_LINK_LOCATOR[STRATEGY_KEY],
                            bl.ADMIN_MENU_CATALOG_LINK_LOCATOR[LOCATOR_KEY])
        self.customers = Link(bl.ADMIN_MENU_CUSTOMERS_LINK_LOCATOR[STRATEGY_KEY],
                              bl.ADMIN_MENU_CUSTOMERS_LINK_LOCATOR[LOCATOR_KEY])
        self.marketing = Link(bl.ADMIN_MENU_MARKETING_LINK_LOCATOR[STRATEGY_KEY],
                              bl.ADMIN_MENU_MARKETING_LINK_LOCATOR[LOCATOR_KEY])
        self.content = Link(bl.ADMIN_MENU_CONTENT_LINK_LOCATOR[STRATEGY_KEY],
                            bl.ADMIN_MENU_CONTENT_LINK_LOCATOR[LOCATOR_KEY])
        self.reports = Link(bl.ADMIN_MENU_REPORTS_LINK_LOCATOR[STRATEGY_KEY],
                            bl.ADMIN_MENU_REPORTS_LINK_LOCATOR[LOCATOR_KEY])
        self.stores = Link(bl.ADMIN_MENU_STORES_LINK_LOCATOR[STRATEGY_KEY],
                           bl.ADMIN_MENU_STORES_LINK_LOCATOR[LOCATOR_KEY])
        self.system = Link(bl.ADMIN_MENU_SYSTEM_LINK_LOCATOR[STRATEGY_KEY],
                           bl.ADMIN_MENU_SYSTEM_LINK_LOCATOR[LOCATOR_KEY])
        self.submenus = {
            bl.SALES_SUBMENU: SalesSubmenu(),
            bl.CATALOG_SUBMENU: CatalogSubmenu(),
            bl.CUSTOMERS_SUBMENU: CustomersSubmenu(),
            bl.MARKETING_SUBMENU: MarketingSubmenu(),
            bl.CONTENT_SUBMENU: ContentSubmenu(),
            bl.REPORTS_SUBMENU: ReportsSubmenu(),
            bl.STORES_SUBMENU: StoresSubmenu(),
            bl.SYSTEM_SUBMENU: SystemSubmenu()
        }

    def submenu(self, key: str):
        return self.submenus[key]
