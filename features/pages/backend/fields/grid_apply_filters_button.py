from features.core_config.backend.backend_locators import GRID_APPLY_FILTERS_BUTTON_LOCATOR
from stere.fields import Button


class GridApplyFiltersButton(Button):
    def __init__(self):
        super().__init__(GRID_APPLY_FILTERS_BUTTON_LOCATOR['strategy'], GRID_APPLY_FILTERS_BUTTON_LOCATOR['locator'])
