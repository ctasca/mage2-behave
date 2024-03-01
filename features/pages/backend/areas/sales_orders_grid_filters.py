from stere.areas import Area
from stere.fields import Root
from features.pages.backend.areas.ui_grids.common_fields import UiGridInterface, GridCommonFields
from ..fields.grid_filters_fields import InputFilter, SelectFilter, DatepickerFilter
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
import features.core_config.backend.backend_locators as bl


class SalesOrdersGridFilters(Area, UiGridInterface):
    COMMON_FIELDS = 'common_fields'
    FILTERS_BUTTON = 'filters_button'
    FULLTEXT_SEARCH_INPUT = 'fulltext_search_input'
    FULLTEXT_SEARCH_BUTTON = 'fulltext_search_button'
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
        self.common_fields = GridCommonFields()
        self.filters_button = self.common_fields.filters_button
        self.apply_filters_button = self.common_fields.apply_filters_button
        self.fulltext_search_input = self.common_fields.fulltext_search_input
        self.fulltext_search_button = self.common_fields.fulltext_search_button
        self.clear_all_filters_button = self.common_fields.clear_all_filters_button
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

    def get_root(self):
        return self.root

    def fulltext_search(self, search_text: str):
        self.common_fields.fulltext_search_input.fill(search_text)
        self.common_fields.fulltext_search_button.click()

    def start_filtering(self):
        self.filters_button.click()

    def get_filter(self, filter_name: str):
        return getattr(self, filter_name)

    def apply_filters(self):
        self.common_fields.apply_filters_button.click()

    def clear_all(self):
        self.common_fields.clear_all_filters_button.click()
