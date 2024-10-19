from typing import Dict

from features.core_config.strategies import STRATEGY_KEY, ID_STRATEGY, LOCATOR_KEY, CSS_STRATEGY

ADMIN_LOGIN_FORM_USERNAME_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "username"}
ADMIN_LOGIN_FORM_PASSWORD_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "login"}
ADMIN_LOGIN_FORM_SIGNIN_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".action-login.action-primary"}
