from stere.areas import Area
from stere.fields import Root
from features.core_config.backend.locators.modal import STRATEGY_KEY, LOCATOR_KEY, ADMIN_NOTIFICATION_MODAL_LOCATOR
from features.pages.backend.fields.admin_notification_modal_fields import AdminNotificationCloseButton


class AdminNotificationModal(Area):
    def __init__(self):
        super().__init__()
        self.root = Root(ADMIN_NOTIFICATION_MODAL_LOCATOR[STRATEGY_KEY], ADMIN_NOTIFICATION_MODAL_LOCATOR[LOCATOR_KEY])
        self.close_button = AdminNotificationCloseButton()

    def click_close_button(self):
        if self.root.is_visible(10) and self.close_button.is_clickable(60):
            self.close_button.click()
