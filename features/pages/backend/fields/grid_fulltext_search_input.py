from features.core_config.backend.backend_locators import GRID_FULLTEXT_INPUT_LOCATOR
from stere.fields import Input


class GridFulltextSearchInput(Input):
    def __init__(self):
        super().__init__(GRID_FULLTEXT_INPUT_LOCATOR['strategy'], GRID_FULLTEXT_INPUT_LOCATOR['locator'])
