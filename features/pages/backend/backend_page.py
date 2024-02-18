from stere import Page
from .areas.admin_menu import AdminMenu

class BackendPage(Page):
    def __init__(self) -> None:
        super().__init__()
        self.admin_menu = AdminMenu()