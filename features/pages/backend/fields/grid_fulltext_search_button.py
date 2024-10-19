from features.core_config.strategies import STRATEGY_KEY, LOCATOR_KEY
from features.core_config.backend.locators.grids import GRID_FULLTEXT_SEARCH_BUTTON_LOCATOR
from stere.fields import Button


class GridFulltextSearchButton(Button):
    def __init__(self):
        super().__init__(GRID_FULLTEXT_SEARCH_BUTTON_LOCATOR[STRATEGY_KEY],
                         GRID_FULLTEXT_SEARCH_BUTTON_LOCATOR[LOCATOR_KEY])
