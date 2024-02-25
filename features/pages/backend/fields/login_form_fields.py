from features.core_config.backend.backend_locators import *
from stere.fields import Input, Button


class Username(Input):
    def __init__(self):
        super().__init__(ADMIN_LOGIN_FORM_USERNAME_LOCATOR['strategy'],
                         ADMIN_LOGIN_FORM_USERNAME_LOCATOR['locator'])


class Password(Input):
    def __init__(self):
        super().__init__(ADMIN_LOGIN_FORM_PASSWORD_LOCATOR['strategy'],
                         ADMIN_LOGIN_FORM_PASSWORD_LOCATOR['locator'])


class SignInButton(Button):
    def __init__(self):
        super().__init__(ADMIN_LOGIN_FORM_SIGNIN_BUTTON_LOCATOR['strategy'],
                         ADMIN_LOGIN_FORM_SIGNIN_BUTTON_LOCATOR['locator'])
