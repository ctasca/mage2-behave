from stere import Page
from .areas.admin_menu import AdminMenu
from .areas.products_grid_filters import ProductsGridFilters
from .ui_grids.common_fields import GridRows, GridCommonActionsFields
from .areas.modal import Modal


class ProductsGrid(Page):
    def __init__(self) -> None:
        super().__init__()
        self.admin_menu = AdminMenu()
        self.grid_filters = ProductsGridFilters()
        self.grid_actions = GridCommonActionsFields()
        self.grid_rows = GridRows()
        self.modal = Modal()
