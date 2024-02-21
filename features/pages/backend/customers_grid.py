from stere import Page
from .areas.admin_menu import AdminMenu
from .fields.grid_filters_button import GridFiltersButton


class CustomersGrid(Page):
    def __init__(self) -> None:
        super().__init__()
        self.admin_menu = AdminMenu()
        self.filters_button = GridFiltersButton()
