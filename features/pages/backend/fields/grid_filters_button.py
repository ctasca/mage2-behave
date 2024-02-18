import core_config.all as config
from stere.areas.repeating_area import RepeatingArea
from stere.fields import Root ,Button

class GridFiltersButton(Button):
    def __init__(self):
        super().__init__(config.GRID_FILTER_BUTTON_LOCATOR['strategy'], config.GRID_FILTER_BUTTON_LOCATOR['locator'])
        