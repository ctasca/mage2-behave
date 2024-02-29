from stere.areas import Area
from stere.fields import Root
from ..fields.grid_filters_fields import InputFilter
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
import features.core_config.backend.backend_locators as bl


class CustomersGridFilters(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.GRID_FILTERS_ROOT_LOCATOR[STRATEGY_KEY], bl.GRID_FILTERS_ROOT_LOCATOR[LOCATOR_KEY])
        self.from_id_input = InputFilter(bl.CUSTOMERS_FROM_ID_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                         bl.CUSTOMERS_FROM_ID_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.to_id_input = InputFilter(bl.CUSTOMERS_TO_ID_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                       bl.CUSTOMERS_TO_ID_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.email_input = InputFilter(bl.CUSTOMERS_EMAIL_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                       bl.CUSTOMERS_EMAIL_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.name_input = InputFilter(bl.CUSTOMERS_NAME_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                      bl.CUSTOMERS_NAME_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.telephone_input = InputFilter(bl.CUSTOMERS_TELEPHONE_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                           bl.CUSTOMERS_TELEPHONE_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
