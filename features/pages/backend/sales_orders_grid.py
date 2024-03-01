from stere import Page
from .areas.admin_menu import AdminMenu
from .areas.sales_orders_grid_filters import SalesOrdersGridFilters


class SalesOrdersGrid(Page):
    def __init__(self) -> None:
        super().__init__()
        self.admin_menu = AdminMenu()
        self.orders_grid_filters = SalesOrdersGridFilters()
