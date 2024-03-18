from stere import Page
from .areas.admin_menu import AdminMenu
from .areas.modal import Modal
from .areas.system_configuration_tabs import SystemConfigurationTabs
from .fields.store_switcher_button import StoreSwitcher
from .fields.system_configuration_save_button import SystemConfigurationSaveButton


class SystemConfiguration(Page):
    def __init__(self) -> None:
        super().__init__()
        self.admin_menu = AdminMenu()
        self.store_switcher = StoreSwitcher()
        self.tabs = SystemConfigurationTabs()
        self.modal = Modal()
        self.save_button = SystemConfigurationSaveButton()
