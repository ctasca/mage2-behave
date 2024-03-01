from stere import Page
from .areas.admin_menu import AdminMenu
from .areas.sales_orders_grid_filters import SalesOrdersGridFilters
from .ui_grids.common_fields import GridRows, GridCommonActionsFields
from .areas.modal import Modal


class SalesOrdersGrid(Page):
    def __init__(self) -> None:
        super().__init__()
        self.admin_menu = AdminMenu()
        self.orders_grid_filters = SalesOrdersGridFilters()
        self.grid_actions = GridCommonActionsFields()
        self.grid_rows = GridRows()
        self.modal = Modal()
