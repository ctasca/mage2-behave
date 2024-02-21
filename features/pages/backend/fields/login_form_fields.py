import features.core_config.all as config
from stere.fields import Input, Button


class Username(Input):
    def __init__(self):
        super().__init__(config.ADMIN_LOGIN_FORM_USERNAME_LOCATOR['strategy'],
                         config.ADMIN_LOGIN_FORM_USERNAME_LOCATOR['locator'])


class Password(Input):
    def __init__(self):
        super().__init__(config.ADMIN_LOGIN_FORM_PASSWORD_LOCATOR['strategy'],
                         config.ADMIN_LOGIN_FORM_PASSWORD_LOCATOR['locator'])


class SignInButton(Button):
    def __init__(self):
        super().__init__(config.ADMIN_LOGIN_FORM_SIGNIN_BUTTON_LOCATOR['strategy'],
                         config.ADMIN_LOGIN_FORM_SIGNIN_BUTTON_LOCATOR['locator'])
