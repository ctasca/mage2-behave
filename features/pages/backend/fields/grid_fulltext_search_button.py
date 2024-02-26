from features.core_config.backend.backend_locators import GRID_FULLTEXT_SEARCH_BUTTON_LOCATOR
from stere.fields import Button


class GridFulltextSearchButton(Button):
    def __init__(self):
        super().__init__(GRID_FULLTEXT_SEARCH_BUTTON_LOCATOR['strategy'],
                         GRID_FULLTEXT_SEARCH_BUTTON_LOCATOR['locator'])
