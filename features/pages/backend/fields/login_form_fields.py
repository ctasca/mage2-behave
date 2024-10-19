from features.core_config.strategies import STRATEGY_KEY, LOCATOR_KEY
from features.core_config.backend.locators.admin_login import ADMIN_LOGIN_FORM_USERNAME_LOCATOR, \
    ADMIN_LOGIN_FORM_PASSWORD_LOCATOR, ADMIN_LOGIN_FORM_SIGNIN_BUTTON_LOCATOR
from stere.fields import Input, Button


class Username(Input):
    def __init__(self):
        super().__init__(ADMIN_LOGIN_FORM_USERNAME_LOCATOR[STRATEGY_KEY],
                         ADMIN_LOGIN_FORM_USERNAME_LOCATOR[LOCATOR_KEY])


class Password(Input):
    def __init__(self):
        super().__init__(ADMIN_LOGIN_FORM_PASSWORD_LOCATOR[STRATEGY_KEY],
                         ADMIN_LOGIN_FORM_PASSWORD_LOCATOR[LOCATOR_KEY])


class SignInButton(Button):
    def __init__(self):
        super().__init__(ADMIN_LOGIN_FORM_SIGNIN_BUTTON_LOCATOR[STRATEGY_KEY],
                         ADMIN_LOGIN_FORM_SIGNIN_BUTTON_LOCATOR[LOCATOR_KEY])
