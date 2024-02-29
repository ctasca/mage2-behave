from stere import Page
from .areas.admin_menu import AdminMenu
from .fields.grid_filters_button import GridFiltersButton
from .fields.grid_fulltext_search_input import GridFulltextSearchInput
from .fields.grid_fulltext_search_button import GridFulltextSearchButton
from .fields.grid_apply_filters_button import GridApplyFiltersButton
from features.pages.backend.fields.grid_clear_all_filters_button import GridActiveFiltersClearAllButton
from .areas.customers_grid_filters import CustomersGridFilters


class CustomersGrid(Page):
    def __init__(self) -> None:
        super().__init__()
        self.admin_menu = AdminMenu()
        self.filters_button = GridFiltersButton()
        self.fulltext_search_input = GridFulltextSearchInput()
        self.fulltext_search_button = GridFulltextSearchButton()
        self.apply_filters_button = GridApplyFiltersButton()
        self.clear_all_filters_button = GridActiveFiltersClearAllButton()
        self.customers_grid_filters = CustomersGridFilters()
