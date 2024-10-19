from features.core_config.backend.locators.grids import (STRATEGY_KEY, LOCATOR_KEY, XPATH_STRATEGY,
                                                         GRID_ACTIONS_BUTTON_LOCATOR, GRID_ACTIONS_LIST_ROOT_LOCATOR,
                                                         GRID_ACTION_XPATH_LOCATOR,
                                                         GRID_ACTIONS_SUBMENU_ROOT_LOCATOR,
                                                         GRID_ACTIONS_SUBMENU_XPATH_LOCATOR)
from stere.fields import Button, Root, Field
from stere.areas import RepeatingArea


class GridActionsButton(Button):
    def __init__(self):
        super().__init__(GRID_ACTIONS_BUTTON_LOCATOR[STRATEGY_KEY], GRID_ACTIONS_BUTTON_LOCATOR[LOCATOR_KEY])


class GridActionsList(RepeatingArea):
    def __init__(self):
        super().__init__(
            root=Root(GRID_ACTIONS_LIST_ROOT_LOCATOR[STRATEGY_KEY], GRID_ACTIONS_LIST_ROOT_LOCATOR[LOCATOR_KEY]),
            action=Field(XPATH_STRATEGY, GRID_ACTION_XPATH_LOCATOR)
        )


class GridSubmenuActionsList(RepeatingArea):
    def __init__(self):
        super().__init__(
            root=Root(GRID_ACTIONS_SUBMENU_ROOT_LOCATOR[STRATEGY_KEY], GRID_ACTIONS_SUBMENU_ROOT_LOCATOR[LOCATOR_KEY]),
            action=Field(XPATH_STRATEGY, GRID_ACTIONS_SUBMENU_XPATH_LOCATOR)
        )
