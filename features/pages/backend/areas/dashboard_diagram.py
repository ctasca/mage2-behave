import features.core_config.backend.backend_locators as bl
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
from stere.areas import Area
from ..fields.dashboard_diagram_tabs import DiagramOrdersTab, DiagramAmountsTab


class DashboardDiagram(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orders_tab = DiagramOrdersTab(bl.DASHBOARD_DIAGRAM_ORDER_TAB_LOCATOR[STRATEGY_KEY],
                                           bl.DASHBOARD_DIAGRAM_ORDER_TAB_LOCATOR[LOCATOR_KEY])
        self.amounts_tab = DiagramAmountsTab(bl.DASHBOARD_DIAGRAM_AMOUNTS_TAB_LOCATOR[STRATEGY_KEY],
                                             bl.DASHBOARD_DIAGRAM_AMOUNTS_TAB_LOCATOR[LOCATOR_KEY])
