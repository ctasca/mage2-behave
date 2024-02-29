from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
from features.core_config.backend.backend_locators import DASHBOARD_RELOAD_DATA_BUTTON_LOCATOR
from stere.fields import Button


class ReloadDataButton(Button):
    def __init__(self):
        super().__init__(DASHBOARD_RELOAD_DATA_BUTTON_LOCATOR[STRATEGY_KEY],
                         DASHBOARD_RELOAD_DATA_BUTTON_LOCATOR[LOCATOR_KEY])
