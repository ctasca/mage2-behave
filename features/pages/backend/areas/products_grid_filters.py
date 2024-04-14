from splinter.exceptions import ElementDoesNotExist
from features.core_config.backend.locators.grids import *
from features.core_config.backend.locators.products_filters import *
from stere.areas import Area
from stere.fields import Root, Field
from features.pages.backend.ui_grids.common_fields import GridCommonFiltersFields
from ..fields.grid_filters_fields import InputFilter, DatepickerFilter, SelectFilter, Button


class AssetFilter(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.select_field = SelectFilter(PRODUCTS_ASSET_SELECT_FILTER_LOCATOR[STRATEGY_KEY],
                                         PRODUCTS_ASSET_SELECT_FILTER_LOCATOR[LOCATOR_KEY])
        self.input_text_field = InputFilter(PRODUCTS_ASSET_SELECT_TEXT_FILTER_LOCATOR[STRATEGY_KEY],
                                            PRODUCTS_ASSET_SELECT_TEXT_FILTER_LOCATOR[LOCATOR_KEY])
        self.option_quantity = Field(PRODUCTS_ASSET_SELECT_FILTER_ITEMS_QUANTITY_LOCATOR[STRATEGY_KEY],
                                     PRODUCTS_ASSET_SELECT_FILTER_ITEMS_QUANTITY_LOCATOR[LOCATOR_KEY])
        self.done_button = Button(PRODUCTS_ASSET_DONE_BUTTON_FILTER_LOCATOR[STRATEGY_KEY],
                                  PRODUCTS_ASSET_DONE_BUTTON_FILTER_LOCATOR[LOCATOR_KEY])

    def _is_active(self) -> bool:
        return self.select_field.has_class('_active')

    def click_select(self):
        if not self._is_active():
            self.select_field.click()

    def search_asset(self, asset: str):
        self.click_select()
        if self._is_active():
            self.input_text_field.fill(asset)

    def assert_options_quantity(self, quantity: int):
        assert self.option_quantity.text == f'{str(quantity)} options'

    def click_option_by_partial_text(self, partial_text: str):
        self.click_option_by_text(partial_text)

    def click_option_by_text(self, text: str):
        if self._is_active():
            filter_option = Field(PRODUCTS_ASSET_SELECT_OPTION_FILTER_LOCATOR_FORMAT[STRATEGY_KEY],
                                  PRODUCTS_ASSET_SELECT_OPTION_FILTER_LOCATOR_FORMAT[LOCATOR_KEY].format(text))
            try:
                checkbox = filter_option.find_by_xpath("./../preceding-sibling::input[@type='checkbox']")
                if not checkbox.checked:
                    filter_option.click()
            except ElementDoesNotExist:
                filter_option.click()

    def done(self):
        if self._is_active():
            self.done_button.click()


class ProductsGridFilters(Area, GridCommonFiltersFields):
    COMMON_FILTER_FIELDS = 'common_filter_fields'
    FILTERS_BUTTON = 'filters_button'
    FULLTEXT_SEARCH_INPUT = 'fulltext_search_input'
    FULLTEXT_SEARCH_BUTTON = 'fulltext_search_button'
    FROM_ID_FILTER = 'from_id_input'
    TO_ID_FILTER = 'to_id_input'
    FROM_PRICE_FILTER = 'from_price_input'
    TO_PRICE_FILTER = 'to_price_input'
    FROM_QUANTITY_FILTER = 'from_quantity_input'
    TO_QUANTITY_FILTER = 'to_quantity_input'
    UPDATED_AT_FROM_FILTER = 'updated_at_from_filter'
    UPDATED_AT_FROM_DATEPICKER_FILTER = 'updated_at_from_datapicker'
    UPDATED_AT_TO_FILTER = 'updated_at_from_filter'
    UPDATED_AT_TO_DATEPICKER_FILTER = 'updated_at_to_datapicker'
    STORE_VIEW_FILTER = 'store_view_select'
    ASSET_FILTER = 'asset_filter'
    NAME_FILTER = 'name_input'
    TYPE_FILTER = 'type_select'
    ATTRIBUTE_SET_FILTER = 'attribute_set_select'
    SKU_FILTER = 'sku_input'
    VISIBILITY_FILTER = 'visibility_select'
    STATUS_FILTER = 'status_select'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(GRID_FILTERS_ROOT_LOCATOR[STRATEGY_KEY], GRID_FILTERS_ROOT_LOCATOR[LOCATOR_KEY])
        self.common_filters_fields = GridCommonFiltersFields()
        self.filters_button = self.common_filters_fields.filters_button
        self.apply_filters_button = self.common_filters_fields.apply_filters_button
        self.fulltext_search_input = self.common_filters_fields.fulltext_search_input
        self.fulltext_search_button = self.common_filters_fields.fulltext_search_button
        self.clear_all_filters_button = self.common_filters_fields.clear_all_filters_button
        self.from_id_input = InputFilter(PRODUCTS_FROM_ID_FILTER_LOCATOR[STRATEGY_KEY],
                                         PRODUCTS_FROM_ID_FILTER_LOCATOR[LOCATOR_KEY])
        self.to_id_input = InputFilter(PRODUCTS_TO_ID_FILTER_LOCATOR[STRATEGY_KEY],
                                       PRODUCTS_TO_ID_FILTER_LOCATOR[LOCATOR_KEY])
        self.from_price_input = InputFilter(PRODUCTS_FROM_PRICE_FILTER_LOCATOR[STRATEGY_KEY],
                                            PRODUCTS_FROM_PRICE_FILTER_LOCATOR[LOCATOR_KEY])
        self.to_price_input = InputFilter(PRODUCTS_TO_PRICE_FILTER_LOCATOR[STRATEGY_KEY],
                                          PRODUCTS_TO_PRICE_FILTER_LOCATOR[LOCATOR_KEY])
        self.from_quantity_input = InputFilter(PRODUCTS_FROM_QTY_FILTER_LOCATOR[STRATEGY_KEY],
                                               PRODUCTS_FROM_QTY_FILTER_LOCATOR[LOCATOR_KEY])
        self.to_quantity_input = InputFilter(PRODUCTS_TO_QTY_FILTER_LOCATOR[STRATEGY_KEY],
                                             PRODUCTS_TO_QTY_FILTER_LOCATOR[LOCATOR_KEY])
        self.updated_at_from_input = InputFilter(PRODUCTS_FROM_LAST_UPDATED_AT_FILTER_LOCATOR[STRATEGY_KEY],
                                                 PRODUCTS_FROM_LAST_UPDATED_AT_FILTER_LOCATOR[LOCATOR_KEY])
        self.updated_at_from_datapicker = DatepickerFilter(GRID_DATEPICKER_BUTTON_LOCATOR[STRATEGY_KEY],
                                                           GRID_DATEPICKER_BUTTON_LOCATOR[LOCATOR_KEY]
                                                           .format('updated_at[from]'))
        self.updated_at_to_input = InputFilter(PRODUCTS_TO_LAST_UPDATED_AT_FILTER_LOCATOR[STRATEGY_KEY],
                                               PRODUCTS_TO_LAST_UPDATED_AT_FILTER_LOCATOR[LOCATOR_KEY])
        self.updated_at_to_datapicker = DatepickerFilter(GRID_DATEPICKER_BUTTON_LOCATOR[STRATEGY_KEY],
                                                         GRID_DATEPICKER_BUTTON_LOCATOR[LOCATOR_KEY]
                                                         .format('updated_at[to]'))
        self.store_view_select = SelectFilter(PRODUCTS_STORE_VIEW_SELECT_FILTER_LOCATOR[STRATEGY_KEY],
                                              PRODUCTS_STORE_VIEW_SELECT_FILTER_LOCATOR[LOCATOR_KEY])
        self.asset_filter = AssetFilter()
        self.name_input = InputFilter(PRODUCTS_NAME_FILTER_LOCATOR[STRATEGY_KEY],
                                      PRODUCTS_NAME_FILTER_LOCATOR[LOCATOR_KEY])
        self.type_select = SelectFilter(PRODUCTS_TYPE_FILTER_LOCATOR[STRATEGY_KEY],
                                        PRODUCTS_TYPE_FILTER_LOCATOR[LOCATOR_KEY])
        self.attribute_set_select = SelectFilter(PRODUCTS_ATTRIBUTE_SET_FILTER_LOCATOR[STRATEGY_KEY],
                                                 PRODUCTS_ATTRIBUTE_SET_FILTER_LOCATOR[LOCATOR_KEY])
        self.sku_input = InputFilter(PRODUCTS_SKU_FILTER_LOCATOR[STRATEGY_KEY],
                                     PRODUCTS_SKU_FILTER_LOCATOR[LOCATOR_KEY])
        self.visibility_select = SelectFilter(PRODUCTS_VISIBILITY_FILTER_LOCATOR[STRATEGY_KEY],
                                              PRODUCTS_VISIBILITY_FILTER_LOCATOR[LOCATOR_KEY])
        self.status_select = SelectFilter(PRODUCTS_STATUS_FILTER_LOCATOR[STRATEGY_KEY],
                                          PRODUCTS_STATUS_FILTER_LOCATOR[LOCATOR_KEY])

    def get_root(self):
        return self.root
