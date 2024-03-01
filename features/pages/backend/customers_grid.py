from stere import Page
from .areas.admin_menu import AdminMenu
from .areas.customers_grid_filters import CustomersGridFilters


class CustomersGrid(Page):
    def __init__(self) -> None:
        super().__init__()
        self.admin_menu = AdminMenu()
        self.customers_grid_filters = CustomersGridFilters()
