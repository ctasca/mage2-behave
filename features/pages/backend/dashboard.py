from stere import Page
from .areas.admin_menu import AdminMenu
from .fields.store_switcher_button import StoreSwitcher


class Dashboard(Page):
    def __init__(self) -> None:
        super().__init__()
        self.admin_menu = AdminMenu()
        self.store_switcher = StoreSwitcher()
