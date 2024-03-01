from stere.areas import RepeatingArea
from stere.fields import Root, Field
from features.core_config.backend.backend_locators import (STRATEGY_KEY, LOCATOR_KEY, XPATH_STRATEGY,
                                                           GRID_ROWS_ROOT_LOCATOR, GRID_ROW_XPATH_LOCATOR)


class GridRowsFields(RepeatingArea):
    def __init__(self):
        super().__init__(
            root=Root(GRID_ROWS_ROOT_LOCATOR[STRATEGY_KEY], GRID_ROWS_ROOT_LOCATOR[LOCATOR_KEY]),
            row=Field(XPATH_STRATEGY, GRID_ROW_XPATH_LOCATOR)
        )

