from features.core_config.backend.locators.admin_menu import *
from features.core_config.backend.locators.admin_submenus import *
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
        self.dashboard = Link(ADMIN_MENU_DASHBOARD_LINK_LOCATOR[STRATEGY_KEY],
                              ADMIN_MENU_DASHBOARD_LINK_LOCATOR[LOCATOR_KEY])
        self.sales = Link(ADMIN_MENU_SALES_LINK_LOCATOR[STRATEGY_KEY],
                          ADMIN_MENU_SALES_LINK_LOCATOR[LOCATOR_KEY])
        self.catalog = Link(ADMIN_MENU_CATALOG_LINK_LOCATOR[STRATEGY_KEY],
                            ADMIN_MENU_CATALOG_LINK_LOCATOR[LOCATOR_KEY])
        self.customers = Link(ADMIN_MENU_CUSTOMERS_LINK_LOCATOR[STRATEGY_KEY],
                              ADMIN_MENU_CUSTOMERS_LINK_LOCATOR[LOCATOR_KEY])
        self.marketing = Link(ADMIN_MENU_MARKETING_LINK_LOCATOR[STRATEGY_KEY],
                              ADMIN_MENU_MARKETING_LINK_LOCATOR[LOCATOR_KEY])
        self.content = Link(ADMIN_MENU_CONTENT_LINK_LOCATOR[STRATEGY_KEY],
                            ADMIN_MENU_CONTENT_LINK_LOCATOR[LOCATOR_KEY])
        self.reports = Link(ADMIN_MENU_REPORTS_LINK_LOCATOR[STRATEGY_KEY],
                            ADMIN_MENU_REPORTS_LINK_LOCATOR[LOCATOR_KEY])
        self.stores = Link(ADMIN_MENU_STORES_LINK_LOCATOR[STRATEGY_KEY],
                           ADMIN_MENU_STORES_LINK_LOCATOR[LOCATOR_KEY])
        self.system = Link(ADMIN_MENU_SYSTEM_LINK_LOCATOR[STRATEGY_KEY],
                           ADMIN_MENU_SYSTEM_LINK_LOCATOR[LOCATOR_KEY])
        self.submenus = {
            SALES_SUBMENU: SalesSubmenu(),
            CATALOG_SUBMENU: CatalogSubmenu(),
            CUSTOMERS_SUBMENU: CustomersSubmenu(),
            MARKETING_SUBMENU: MarketingSubmenu(),
            CONTENT_SUBMENU: ContentSubmenu(),
            REPORTS_SUBMENU: ReportsSubmenu(),
            STORES_SUBMENU: StoresSubmenu(),
            SYSTEM_SUBMENU: SystemSubmenu()
        }

    def submenu(self, key: str):
        return self.submenus[key]

    def get_link(self, link: str):
        return getattr(self, link)
