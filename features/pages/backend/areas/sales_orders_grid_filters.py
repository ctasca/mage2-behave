from features.core_config.backend.locators.grids import *
from features.core_config.backend.locators.orders_filters import *
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.ui_grids.common_fields import UiGridFiltersInterface, GridCommonFiltersFields
from ..fields.grid_filters_fields import InputFilter, DatepickerFilter, SelectFilter


class SalesOrdersGridFilters(Area, GridCommonFiltersFields):
    COMMON_FILTER_FIELDS = 'common_filter_fields'
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
    PURCHASE_POINT = 'purchase_point'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(GRID_FILTERS_ROOT_LOCATOR[STRATEGY_KEY], GRID_FILTERS_ROOT_LOCATOR[LOCATOR_KEY])
        self.common_filters_fields = GridCommonFiltersFields()
        self.filters_button = self.common_filters_fields.filters_button
        self.apply_filters_button = self.common_filters_fields.apply_filters_button
        self.fulltext_search_input = self.common_filters_fields.fulltext_search_input
        self.fulltext_search_button = self.common_filters_fields.fulltext_search_button
        self.clear_all_filters_button = self.common_filters_fields.clear_all_filters_button
        self.created_at_from_input = InputFilter(ORDERS_PURCHASE_DATE_FROM_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                                 ORDERS_PURCHASE_DATE_FROM_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.created_at_from_datapicker = DatepickerFilter(GRID_DATEPICKER_BUTTON_LOCATOR[STRATEGY_KEY],
                                                           GRID_DATEPICKER_BUTTON_LOCATOR[LOCATOR_KEY]
                                                           .format('created_at[from]'))
        self.created_at_to_input = InputFilter(ORDERS_PURCHASE_DATE_TO_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                               ORDERS_PURCHASE_DATE_TO_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.created_at_to_datapicker = DatepickerFilter(GRID_DATEPICKER_BUTTON_LOCATOR[STRATEGY_KEY],
                                                         GRID_DATEPICKER_BUTTON_LOCATOR[LOCATOR_KEY]
                                                         .format('created_at[to]'))
        self.base_grand_total_from = InputFilter(ORDERS_BASE_GRAND_TOTAL_FROM_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                                 ORDERS_BASE_GRAND_TOTAL_FROM_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.base_grand_total_to = InputFilter(ORDERS_BASE_GRAND_TOTAL_TO_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                               ORDERS_BASE_GRAND_TOTAL_TO_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.purchased_grand_total_from = InputFilter(
            ORDERS_PURCHASED_GRAND_TOTAL_FROM_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
            ORDERS_PURCHASED_GRAND_TOTAL_FROM_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.purchased_grand_total_to = InputFilter(
            ORDERS_PURCHASED_GRAND_TOTAL_TO_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
            ORDERS_PURCHASED_GRAND_TOTAL_TO_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.purchase_point = SelectFilter(ORDERS_PURCHASE_POINT_SELECT_FILTER_LOCATOR[STRATEGY_KEY],
                                           ORDERS_PURCHASE_POINT_SELECT_FILTER_LOCATOR[LOCATOR_KEY])

    def get_root(self):
        return self.root
