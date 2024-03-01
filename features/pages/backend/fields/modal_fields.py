from features.core_config.backend.backend_locators import (STRATEGY_KEY, LOCATOR_KEY, MODAL_OK_BUTTON_LOCATOR,
                                                           MODAL_CANCEL_BUTTON_LOCATOR)
from stere.fields import Button


class ModalOkButton(Button):
    def __init__(self):
        super().__init__(MODAL_OK_BUTTON_LOCATOR[STRATEGY_KEY], MODAL_OK_BUTTON_LOCATOR[LOCATOR_KEY])


class ModalCancelButton(Button):
    def __init__(self):
        super().__init__(MODAL_CANCEL_BUTTON_LOCATOR[STRATEGY_KEY], MODAL_CANCEL_BUTTON_LOCATOR[LOCATOR_KEY])
