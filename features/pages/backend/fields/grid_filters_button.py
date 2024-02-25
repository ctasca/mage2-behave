from features.core_config.backend.backend_locators import *
from stere.fields import Button


class GridFiltersButton(Button):
    def __init__(self):
        super().__init__(GRID_FILTER_BUTTON_LOCATOR['strategy'], GRID_FILTER_BUTTON_LOCATOR['locator'])
