import core_config.all as config
from stere.fields import Link
from stere.areas import Area

from .admin_menu_submenus.sales_submenu import SalesSubmenu
from .admin_menu_submenus.catalog_submenu import CatalogSubmenu
from .admin_menu_submenus.customers_submenu import CustomersSubmenu
from .admin_menu_submenus.marketing_submenu import MarketingSubmenu
from .admin_menu_submenus.content_submenu import ContentSubmenu
from .admin_menu_submenus.reports_submenu import ReportsSubmenu

class AdminMenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dashboard = Link(config.ADMIN_MENU_DASHBOARD_LINK_LOCATOR['strategy'], config.ADMIN_MENU_DASHBOARD_LINK_LOCATOR['locator'])
        self.sales = Link(config.ADMIN_MENU_SALES_LINK_LOCATOR['strategy'], config.ADMIN_MENU_SALES_LINK_LOCATOR['locator'])
        self.catalog = Link(config.ADMIN_MENU_CATALOG_LINK_LOCATOR['strategy'], config.ADMIN_MENU_CATALOG_LINK_LOCATOR['locator'])
        self.customers = Link(config.ADMIN_MENU_CUSTOMERS_LINK_LOCATOR['strategy'], config.ADMIN_MENU_CUSTOMERS_LINK_LOCATOR['locator'])
        self.marketing = Link(config.ADMIN_MENU_MARKETING_LINK_LOCATOR['strategy'], config.ADMIN_MENU_MARKETING_LINK_LOCATOR['locator'])
        self.content = Link(config.ADMIN_MENU_CONTENT_LINK_LOCATOR['strategy'], config.ADMIN_MENU_CONTENT_LINK_LOCATOR['locator'])
        self.reports = Link(config.ADMIN_MENU_REPORTS_LINK_LOCATOR['strategy'], config.ADMIN_MENU_REPORTS_LINK_LOCATOR['locator'])
        self.stores = Link(config.ADMIN_MENU_STORES_LINK_LOCATOR['strategy'], config.ADMIN_MENU_STORES_LINK_LOCATOR['locator'])
        self.system = Link(config.ADMIN_MENU_SYSTEM_LINK_LOCATOR['strategy'], config.ADMIN_MENU_SYSTEM_LINK_LOCATOR['locator'])
        self.submenus = {
            'sales': SalesSubmenu(),
            'catalog': CatalogSubmenu(),
            'customers': CustomersSubmenu(),
            'marketing': MarketingSubmenu(),
            'content': ContentSubmenu(),
            'reports': ReportsSubmenu()
        }
        