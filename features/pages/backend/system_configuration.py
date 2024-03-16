from stere import Page
from .areas.admin_menu import AdminMenu
from .areas.system_configuration_tabs import SystemConfigurationTabs


class SystemConfiguration(Page):
    def __init__(self) -> None:
        super().__init__()
        self.admin_menu = AdminMenu()
        self.tabs = SystemConfigurationTabs()
