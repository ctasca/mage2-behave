import features.core_config.backend.backend_locators as bl
from stere.areas import Area
from stere.fields import Root
from ..fields.customers_grid_filters_fields import FromIdInput, ToIdInput


class CustomersGridFilters(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.GRID_FILTERS_ROOT_LOCATOR['strategy'], bl.GRID_FILTERS_ROOT_LOCATOR['locator'])
        self.from_id_input = FromIdInput(bl.CUSTOMERS_FROM_ID_INPUT_LOCATOR['strategy'],
                                         bl.CUSTOMERS_FROM_ID_INPUT_LOCATOR['locator'])
        self.to_id_input = FromIdInput(bl.CUSTOMERS_TO_ID_INPUT_LOCATOR['strategy'],
                                       bl.CUSTOMERS_TO_ID_INPUT_LOCATOR['locator'])
