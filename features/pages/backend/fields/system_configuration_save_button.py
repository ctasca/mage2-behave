from stere.fields import Button
from features.core_config.backend.locators.system_configuration import STRATEGY_KEY, LOCATOR_KEY, SAVE_BUTTON_LOCATOR


class SystemConfigurationSaveButton(Button):
    def __init__(self):
        super().__init__(SAVE_BUTTON_LOCATOR[STRATEGY_KEY],
                         SAVE_BUTTON_LOCATOR[LOCATOR_KEY])
