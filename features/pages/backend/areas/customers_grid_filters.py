from stere.areas import Area
from stere.fields import Root
from features.pages.backend.areas.ui_grids.common_fields import UiGridFiltersInterface, GridCommonFields
from ..fields.grid_filters_fields import InputFilter, SelectFilter, DatepickerFilter
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
import features.core_config.backend.backend_locators as bl


class CustomersGridFiltersFilters(Area, UiGridFiltersInterface):
    COMMON_FIELDS = 'common_fields'
    FILTERS_BUTTON = 'filters_button'
    FULLTEXT_SEARCH_INPUT = 'fulltext_search_input'
    FULLTEXT_SEARCH_BUTTON = 'fulltext_search_button'
    FROM_ID_FILTER = 'from_id_input'
    TO_ID_FILTER = 'to_id_input'
    EMAIL_FILTER = 'email_input'
    NAME_FILTER = 'name_input'
    TELEPHONE_FILTER = 'telephone_input'
    POSTCODE_FILTER = 'postcode_input'
    REGION_FILTER = 'region_input'
    TAX_VAT_FILTER = 'tax_vat_input'
    CREATED_AT_FROM_FILTER = 'created_at_from_input'
    CREATED_AT_FROM_DATAPICKER = 'created_at_from_datapicker'
    CREATED_AT_TO_FILTER = 'created_at_to_input'
    CREATED_AT_TO_DATAPICKER = 'created_at_to_datapicker'
    DOB_FROM_FILTER = 'dob_from_input'
    DOB_FROM_DATAPICKER = 'dob_from_datapicker'
    DOB_TO_FILTER = 'dob_to_input'
    DOB_TO_DATAPICKER = 'dob_to_datapicker'
    GROUP_ID_FILTER = 'group_id_select'
    COUNTRY_ID_FILTER = 'country_id_select'
    WEBSITE_ID_FILTER = 'website_id_select'
    GENDER_FILTER = 'gender_select'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.GRID_FILTERS_ROOT_LOCATOR[STRATEGY_KEY], bl.GRID_FILTERS_ROOT_LOCATOR[LOCATOR_KEY])
        self.common_fields = GridCommonFields()
        self.filters_button = self.common_fields.filters_button
        self.apply_filters_button = self.common_fields.apply_filters_button
        self.fulltext_search_input = self.common_fields.fulltext_search_input
        self.fulltext_search_button = self.common_fields.fulltext_search_button
        self.clear_all_filters_button = self.common_fields.clear_all_filters_button
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
        self.postcode_input = InputFilter(bl.CUSTOMERS_POSTCODE_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                          bl.CUSTOMERS_POSTCODE_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.region_input = InputFilter(bl.CUSTOMERS_REGION_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                        bl.CUSTOMERS_REGION_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.tax_vat_input = InputFilter(bl.CUSTOMERS_TAX_VAT_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                         bl.CUSTOMERS_TAX_VAT_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.created_at_from_input = InputFilter(bl.CUSTOMERS_CREATED_FROM_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                                 bl.CUSTOMERS_CREATED_TO_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.created_at_from_datapicker = DatepickerFilter(bl.GRID_DATEPICKER_BUTTON_LOCATOR[STRATEGY_KEY],
                                                           bl.GRID_DATEPICKER_BUTTON_LOCATOR[LOCATOR_KEY]
                                                           .format('created_at[from]'))
        self.created_at_to_input = InputFilter(bl.GRID_DATEPICKER_BUTTON_LOCATOR[STRATEGY_KEY],
                                               bl.GRID_DATEPICKER_BUTTON_LOCATOR[LOCATOR_KEY])
        self.created_at_to_datapicker = DatepickerFilter(bl.GRID_DATEPICKER_BUTTON_LOCATOR[STRATEGY_KEY],
                                                         bl.GRID_DATEPICKER_BUTTON_LOCATOR[LOCATOR_KEY]
                                                         .format('created_at[to]'))
        self.dob_from_input = InputFilter(bl.CUSTOMERS_DOB_FROM_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                          bl.CUSTOMERS_DOB_FROM_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.dob_from_datapicker = DatepickerFilter(bl.GRID_DATEPICKER_BUTTON_LOCATOR[STRATEGY_KEY],
                                                    bl.GRID_DATEPICKER_BUTTON_LOCATOR[LOCATOR_KEY].format(
                                                        'dob[from]'))
        self.dob_to_input = InputFilter(bl.CUSTOMERS_DOB_TO_INPUT_FILTER_LOCATOR[STRATEGY_KEY],
                                        bl.CUSTOMERS_DOB_TO_INPUT_FILTER_LOCATOR[LOCATOR_KEY])
        self.dob_to_datapicker = DatepickerFilter(bl.GRID_DATEPICKER_BUTTON_LOCATOR[STRATEGY_KEY],
                                                  bl.GRID_DATEPICKER_BUTTON_LOCATOR[LOCATOR_KEY].format('dob[to]'))
        self.group_id_select = SelectFilter(bl.CUSTOMERS_GROUP_SELECT_FILTER_LOCATOR[STRATEGY_KEY],
                                            bl.CUSTOMERS_GROUP_SELECT_FILTER_LOCATOR[LOCATOR_KEY])
        self.country_id_select = SelectFilter(bl.CUSTOMERS_COUNTRY_SELECT_FILTER_LOCATOR[STRATEGY_KEY],
                                              bl.CUSTOMERS_COUNTRY_SELECT_FILTER_LOCATOR[LOCATOR_KEY])
        self.website_id_select = SelectFilter(bl.CUSTOMERS_WEBSITE_SELECT_FILTER_LOCATOR[STRATEGY_KEY],
                                              bl.CUSTOMERS_WEBSITE_SELECT_FILTER_LOCATOR[LOCATOR_KEY])
        self.gender_select = SelectFilter(bl.CUSTOMERS_GENDER_SELECT_FILTER_LOCATOR[STRATEGY_KEY],
                                          bl.CUSTOMERS_GENDER_SELECT_FILTER_LOCATOR[LOCATOR_KEY])

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
