from features.core_config.backend.locators.grids import STRATEGY_KEY, LOCATOR_KEY, GRID_CLEAR_ALL_FILTERS_BUTTON_LOCATOR
from stere.fields import Button


class GridActiveFiltersClearAllButton(Button):
    def __init__(self):
        super().__init__(GRID_CLEAR_ALL_FILTERS_BUTTON_LOCATOR[STRATEGY_KEY],
                         GRID_CLEAR_ALL_FILTERS_BUTTON_LOCATOR[LOCATOR_KEY])
