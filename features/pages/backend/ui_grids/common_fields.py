from abc import ABC, abstractmethod
from stere.fields import Checkbox
from features.core_config.backend.backend_locators import STRATEGY_KEY, LOCATOR_KEY, GRID_ROW_CHECKBOX_LOCATOR
from features.pages.backend.fields.grid_filters_button import GridFiltersButton
from features.pages.backend.fields.grid_fulltext_search_input import GridFulltextSearchInput
from features.pages.backend.fields.grid_fulltext_search_button import GridFulltextSearchButton
from features.pages.backend.fields.grid_apply_filters_button import GridApplyFiltersButton
from features.pages.backend.fields.grid_clear_all_filters_button import GridActiveFiltersClearAllButton
from features.pages.backend.fields.grid_actions_fields import GridActionsButton, GridActionsList
from features.pages.backend.fields.grid_rows_fields import GridRowsFields


class UiGridFiltersInterface(ABC):
    @abstractmethod
    def fulltext_search(self, search_text: str):
        pass

    @abstractmethod
    def start_filtering(self):
        pass

    @abstractmethod
    def get_filter(self, filter_name: str):
        pass

    @abstractmethod
    def apply_filters(self):
        pass

    @abstractmethod
    def clear_all(self):
        pass


class UiGridActionsInterface(ABC):
    @abstractmethod
    def click_actions_button(self):
        pass

    @abstractmethod
    def click_action(self, action_name: str):
        pass


class UiGridRowsInterface(ABC):
    @abstractmethod
    def click_row_checkbox(self, row_index: int):
        pass


class GridCommonFiltersFields(UiGridFiltersInterface):
    def __init__(self):
        self.filters_button = GridFiltersButton()
        self.fulltext_search_input = GridFulltextSearchInput()
        self.fulltext_search_button = GridFulltextSearchButton()
        self.apply_filters_button = GridApplyFiltersButton()
        self.clear_all_filters_button = GridActiveFiltersClearAllButton()

    def fulltext_search(self, search_text: str):
        self.fulltext_search_input.fill(search_text)
        self.fulltext_search_button.click()

    def start_filtering(self):
        self.filters_button.click()

    def get_filter(self, filter_name: str):
        return getattr(self, filter_name)

    def apply_filters(self):
        self.apply_filters_button.click()

    def clear_all(self):
        self.clear_all_filters_button.click()


class GridCommonActionsFields(UiGridActionsInterface):
    def __init__(self):
        self.actions_button = GridActionsButton()
        self.actions_list = GridActionsList()

    def click_actions_button(self):
        self.actions_button.click()

    def click_action(self, action_name: str):
        actions = self.actions_list.children()
        for action in actions:
            if action.action.value_contains(action_name):
                action.action.click()
                break


class GridRows(UiGridRowsInterface):
    def __init__(self):
        self.rows = GridRowsFields()

    def click_row_checkbox(self, row_index: int):
        checkbox = Checkbox(GRID_ROW_CHECKBOX_LOCATOR[STRATEGY_KEY],
                            GRID_ROW_CHECKBOX_LOCATOR[LOCATOR_KEY].format(row_index))
        checkbox.set_to(True)
