from stere.areas import RepeatingArea
from stere.fields import Root, Checkbox
from features.core_config.backend.locators.grids import (STRATEGY_KEY, LOCATOR_KEY, XPATH_STRATEGY,
                                                         GRID_ROWS_ROOT_LOCATOR, GRID_ROW_CHECKBOX_LOCATOR)


class GridRowsFields(RepeatingArea):
    def __init__(self):
        super().__init__(
            root=Root(GRID_ROWS_ROOT_LOCATOR[STRATEGY_KEY], GRID_ROWS_ROOT_LOCATOR[LOCATOR_KEY]),
            checkbox=Checkbox(XPATH_STRATEGY, GRID_ROW_CHECKBOX_LOCATOR)
        )
