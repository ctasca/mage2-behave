from features.core_config.backend.backend_locators import GRID_ACTIVE_FILTERS_ROOT_LOCATOR, GRID_ACTIVE_FILERS_BUTTON_LOCATOR
from stere.areas import RepeatingArea
from stere.fields import Root, Button


class GridActiveFiltersButtons(RepeatingArea):
    """
    This class is inheriting from Repeating
    to create a grid of active filters and associate a removal button for each.
    """
    def __init__(self):
        super().__init__(
            root=Root(GRID_ACTIVE_FILTERS_ROOT_LOCATOR['strategy'], GRID_ACTIVE_FILTERS_ROOT_LOCATOR['locator']),
            remove_button=Button(
                GRID_ACTIVE_FILERS_BUTTON_LOCATOR['strategy'],
                GRID_ACTIVE_FILERS_BUTTON_LOCATOR['locator']
            )
        )

