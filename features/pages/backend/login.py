from stere import Page
from .areas.login_form import LoginForm

class Login(Page):
    def __init__(self):
        self.form = LoginForm()