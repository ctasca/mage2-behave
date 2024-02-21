import features.core_config.all as config
from stere.fields import Button


class GridFiltersButton(Button):
    def __init__(self):
        super().__init__(config.GRID_FILTER_BUTTON_LOCATOR['strategy'], config.GRID_FILTER_BUTTON_LOCATOR['locator'])
