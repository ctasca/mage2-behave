from features.core_config.backend.backend_locators import GRID_CLEAR_ALL_FILTERS_BUTTON_LOCATOR
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
from stere.fields import Button


class GridActiveFiltersClearAllButton(Button):
    def __init__(self):
        super().__init__(GRID_CLEAR_ALL_FILTERS_BUTTON_LOCATOR[STRATEGY_KEY],
                         GRID_CLEAR_ALL_FILTERS_BUTTON_LOCATOR[LOCATOR_KEY])
