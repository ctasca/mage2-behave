from stere.areas import Area
from features.pages.backend.fields.login_form_fields import Username, Password, SignInButton


class LoginForm(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = Username()
        self.password = Password()
        self.signin = SignInButton()
