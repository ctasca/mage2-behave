from features.core_config.config import *
from stere.fields import Button


class ReloadDataButton(Button):
    def __init__(self):
        super().__init__(DASHBOARD_RELOAD_DATA_BUTTON_LOCATOR['strategy'],
                         DASHBOARD_RELOAD_DATA_BUTTON_LOCATOR['locator'])
