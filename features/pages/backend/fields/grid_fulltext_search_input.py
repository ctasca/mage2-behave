from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
from features.core_config.backend.backend_locators import GRID_FULLTEXT_INPUT_LOCATOR
from stere.fields import Input


class GridFulltextSearchInput(Input):
    def __init__(self):
        super().__init__(GRID_FULLTEXT_INPUT_LOCATOR[STRATEGY_KEY], GRID_FULLTEXT_INPUT_LOCATOR[LOCATOR_KEY])
