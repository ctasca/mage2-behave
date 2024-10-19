from stere.fields import Field
from features.core_config.backend.locators.spinners import STRATEGY_KEY, LOCATOR_KEY, SPINNER_DATA_ROLE_LOCATOR


class SpinnerDivisionField(Field):
    def __init__(self):
        super().__init__(SPINNER_DATA_ROLE_LOCATOR[STRATEGY_KEY],
                         SPINNER_DATA_ROLE_LOCATOR[LOCATOR_KEY])
