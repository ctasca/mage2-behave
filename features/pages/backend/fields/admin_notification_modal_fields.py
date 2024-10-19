from features.core_config.backend.locators.modal import (STRATEGY_KEY, LOCATOR_KEY,
                                                         ADMIN_NOTIFICATION_CLOSE_BUTTON_LOCATOR)
from stere.fields import Button


class AdminNotificationCloseButton(Button):
    def __init__(self):
        super().__init__(ADMIN_NOTIFICATION_CLOSE_BUTTON_LOCATOR[STRATEGY_KEY],
                         ADMIN_NOTIFICATION_CLOSE_BUTTON_LOCATOR[LOCATOR_KEY])
