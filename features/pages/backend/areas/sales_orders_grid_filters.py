from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.grid_clear_all_filters_button import GridActiveFiltersClearAllButton
from ..fields.grid_filters_fields import InputFilter, SelectFilter, DatepickerFilter
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
import features.core_config.backend.backend_locators as bl


class SalesOrdersGridFilters(Area):
    CREATED_AT_FROM_INPUT = 'created_at_from_input'
    CREATED_AT_FROM_DATAPICKER = 'created_at_from_datapicker'
    CREATED_AT_TO_INPUT = 'created_at_to_input'
    CREATED_AT_TO_DATAPICKER = 'created_at_to_datapicker'
    BASE_GRAND_TOTAL_FROM = 'base_grand_total_from'
    BASE_GRAND_TOTAL_TO = 'base_grand_total_to'
    PURCHASED_GRAND_TOTAL_FROM = 'purchased_grand_total_from'
    PURCHASED_GRAND_TOTAL_TO = 'purchased_grand_total_to'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.GRID_FILTERS_ROOT_LOCATOR[STRATEGY_KEY], bl.GRID_FILTERS_ROOT_LOCATOR[LOCATOR_KEY])
        self.created_at_from_input = InputFilter(bl.ORDERS_PURCHASE_DATE_FROM_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                                 bl.ORDERS_PURCHASE_DATE_FROM_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.created_at_from_datapicker = DatepickerFilter(bl.GRID_DATEPICKER_BUTTON_LOCATOR[STRATEGY_KEY],
                                                           bl.GRID_DATEPICKER_BUTTON_LOCATOR[LOCATOR_KEY]
                                                           .format('created_at[from]'))
        self.created_at_to_input = InputFilter(bl.ORDERS_PURCHASE_DATE_TO_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                               bl.ORDERS_PURCHASE_DATE_TO_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.created_at_to_datapicker = DatepickerFilter(bl.GRID_DATEPICKER_BUTTON_LOCATOR[STRATEGY_KEY],
                                                         bl.GRID_DATEPICKER_BUTTON_LOCATOR[LOCATOR_KEY]
                                                         .format('created_at[to]'))
        self.base_grand_total_from = InputFilter(bl.ORDERS_BASE_GRAND_TOTAL_FROM_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                                 bl.ORDERS_BASE_GRAND_TOTAL_FROM_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.base_grand_total_to = InputFilter(bl.ORDERS_BASE_GRAND_TOTAL_TO_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                               bl.ORDERS_BASE_GRAND_TOTAL_TO_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.purchased_grand_total_from = InputFilter(
            bl.ORDERS_PURCHASED_GRAND_TOTAL_FROM_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
            bl.ORDERS_PURCHASED_GRAND_TOTAL_FROM_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.purchased_grand_total_to = InputFilter(
            bl.ORDERS_PURCHASED_GRAND_TOTAL_TO_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
            bl.ORDERS_PURCHASED_GRAND_TOTAL_TO_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.clear_all_filters_button = GridActiveFiltersClearAllButton()

    def get_root(self):
        return self.root

    def get_filter(self, filter_name):
        return getattr(self, filter_name)

    def clear_all(self):
        self.clear_all_filters_button.click()
