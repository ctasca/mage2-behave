import core_config.all as config
from stere.fields import Input, Button

class Username(Input):
    def __init__(self):
        super().__init__('id', config.ADMIN_LOGIN_FORM_USERNAME_LOCATOR)

class Password(Input):
    def __init__(self):
        super().__init__('id', config.ADMIN_LOGIN_FORM_PASSWORD_LOCATOR)

class SignInButton(Button):
    def __init__(self):
        super().__init__('css', config.ADMIN_LOGIN_FORM_SIGNIN_BUTTON_LOCATOR)