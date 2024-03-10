from features.core_config.backend.locators.dashboard import *
from features.core_config.strategies import STRATEGY_KEY, LOCATOR_KEY
from stere.areas import Area
from ..fields.dashboard_diagram_tabs import DiagramOrdersTab, DiagramAmountsTab


class DashboardDiagram(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orders_tab = DiagramOrdersTab(DASHBOARD_DIAGRAM_ORDER_TAB_LOCATOR[STRATEGY_KEY],
                                           DASHBOARD_DIAGRAM_ORDER_TAB_LOCATOR[LOCATOR_KEY])
        self.amounts_tab = DiagramAmountsTab(DASHBOARD_DIAGRAM_AMOUNTS_TAB_LOCATOR[STRATEGY_KEY],
                                             DASHBOARD_DIAGRAM_AMOUNTS_TAB_LOCATOR[LOCATOR_KEY])
