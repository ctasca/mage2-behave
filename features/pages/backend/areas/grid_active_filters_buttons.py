from features.core_config.backend.backend_locators import (GRID_ACTIVE_FILTERS_ROOT_LOCATOR,
                                                           GRID_ACTIVE_FILERS_BUTTON_LOCATOR)
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
from stere.areas import RepeatingArea
from stere.fields import Root, Button


class GridActiveFiltersButtons(RepeatingArea):
    """
    This class is inheriting from RepeatingArea
    to create a grid of active filters and associate a removal button for each.
    """
    def __init__(self):
        super().__init__(
            root=Root(GRID_ACTIVE_FILTERS_ROOT_LOCATOR[STRATEGY_KEY], GRID_ACTIVE_FILTERS_ROOT_LOCATOR[LOCATOR_KEY]),
            remove_button=Button(
                GRID_ACTIVE_FILERS_BUTTON_LOCATOR[STRATEGY_KEY],
                GRID_ACTIVE_FILERS_BUTTON_LOCATOR[LOCATOR_KEY]
            )
        )
