from .backend_page import BackendPage
from .fields.grid_filters_button import GridFiltersButton

class CustomersGrid(BackendPage):
    def __init__(self) -> None:
        super().__init__()
        self.filters_button = GridFiltersButton()