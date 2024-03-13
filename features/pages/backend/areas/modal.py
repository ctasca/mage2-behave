from stere.areas import Area
from features.pages.backend.fields.modal_fields import ModalOkButton, ModalCancelButton


class Modal(Area):
    def __init__(self):
        super().__init__()
        self.ok_button = ModalOkButton()
        self.cancel_button = ModalCancelButton()

    def click_ok_button(self):
        self.ok_button.is_clickable(10)
        self.ok_button.click()

    def click_cancel_button(self):
        self.cancel_button.is_clickable(10)
        self.cancel_button.click()
