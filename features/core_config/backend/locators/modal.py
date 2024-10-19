from typing import Dict

from features.core_config.strategies import STRATEGY_KEY, XPATH_STRATEGY, CSS_STRATEGY, LOCATOR_KEY

MODAL_OK_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//button[@data-role='action' and contains(@class, 'action-accept')]"}
MODAL_CANCEL_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//button[@data-role='action' and contains(@class, 'action-dismiss')]"}
ADMIN_NOTIFICATION_MODAL_LOCATOR: Dict[str, str] = {STRATEGY_KEY: CSS_STRATEGY,
                                                    LOCATOR_KEY: ".modal-popup.modal-system-messages"}
ADMIN_NOTIFICATION_CLOSE_BUTTON_LOCATOR: Dict[str, str] = {STRATEGY_KEY: XPATH_STRATEGY,
                                                           LOCATOR_KEY: "(//button[@data-role='closeBtn'])[1]"}
