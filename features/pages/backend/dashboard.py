from stere import Page
from .areas.admin_menu import AdminMenu
from .areas.dashboard_diagram import DashboardDiagram
from .areas.dashboard_store_stats import DashboardStoreStats
from .fields.store_switcher_button import StoreSwitcher
from .fields.reload_data_button import ReloadDataButton
from .areas.admin_notification_modal import AdminNotificationModal
from .fields.spinner_division_field import SpinnerDivisionField


class Dashboard(Page):
    def __init__(self) -> None:
        super().__init__()
        self.spinner = SpinnerDivisionField()
        self.admin_menu = AdminMenu()
        self.store_switcher = StoreSwitcher()
        self.reload_data_button = ReloadDataButton()
        self.dashboard_diagram = DashboardDiagram()
        self.dashboard_store_stats = DashboardStoreStats()
        self.admin_notification_modal = AdminNotificationModal()
