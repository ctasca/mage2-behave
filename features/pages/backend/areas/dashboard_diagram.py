from features.core_config.config import *
from stere.areas import Area
from ..fields.dashboard_diagram_tabs import DiagramOrdersTab, DiagramAmountsTab


class DashboardDiagram(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orders_tab = DiagramOrdersTab(DASHBOARD_DIAGRAM_ORDER_TAB_LOCATOR['strategy'],
                                           DASHBOARD_DIAGRAM_ORDER_TAB_LOCATOR['locator'])
        self.amounts_tab = DiagramAmountsTab(DASHBOARD_DIAGRAM_AMOUNTS_TAB_LOCATOR['strategy'],
                                            DASHBOARD_DIAGRAM_AMOUNTS_TAB_LOCATOR['locator'])
