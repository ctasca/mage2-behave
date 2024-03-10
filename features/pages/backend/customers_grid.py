from stere import Page
from .areas.admin_menu import AdminMenu
from .areas.customers_grid_filters import CustomersGridFilters
from .ui_grids.common_fields import GridRows, GridCommonActionsFields
from .areas.modal import Modal


class CustomersGrid(Page):
    def __init__(self) -> None:
        super().__init__()
        self.admin_menu = AdminMenu()
        self.grid_filters = CustomersGridFilters()
        self.grid_actions = GridCommonActionsFields()
        self.grid_rows = GridRows()
        self.modal = Modal()

