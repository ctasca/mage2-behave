import time
from abc import ABC, abstractmethod
from stere.fields import Field
from features.core_config.strategies import STRATEGY_KEY, LOCATOR_KEY
from features.core_config.backend.locators.grids import GRID_LOADING_MASK_LOCATOR
from features.pages.backend.fields.grid_filters_button import GridFiltersButton
from features.pages.backend.fields.grid_fulltext_search_input import GridFulltextSearchInput
from features.pages.backend.fields.grid_fulltext_search_button import GridFulltextSearchButton
from features.pages.backend.fields.grid_apply_filters_button import GridApplyFiltersButton
from features.pages.backend.fields.grid_clear_all_filters_button import GridActiveFiltersClearAllButton
from features.pages.backend.fields.grid_actions_fields import GridActionsButton, GridActionsList, GridSubmenuActionsList
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
    def apply_filters(self, implicit_wait: int = 0):
        pass

    @abstractmethod
    def clear_all(self, implicit_wait: int = 0):
        pass


class UiGridActionsInterface(ABC):
    @abstractmethod
    def click_actions_button(self):
        pass

    @abstractmethod
    def click_action(self, action_name: str):
        pass

    @abstractmethod
    def click_sub_action(self, action_name: str):
        pass


class UiGridRowsInterface(ABC):
    @abstractmethod
    def click_row_checkbox(self, row_index: int, set_to: bool):
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

    def apply_filters(self, implicit_wait: int = 0):
        self.apply_filters_button.click()
        time.sleep(implicit_wait)

    def clear_all(self, implicit_wait: int = 0):
        self.clear_all_filters_button.click()
        time.sleep(implicit_wait)


class GridCommonActionsFields(UiGridActionsInterface):

    def __init__(self):
        self.actions_button = GridActionsButton()
        self.actions_list = GridActionsList()
        self.submenu_actions_list = GridSubmenuActionsList()

    def click_actions_button(self):
        self.actions_button.click()

    def click_action(self, action_name: str):
        actions = self.actions_list.children()
        for action in actions:
            if action.action.text == action_name:
                action.action.click()
                break

    def click_sub_action(self, action_name: str):
        actions = self.submenu_actions_list.children()
        for action in actions:
            if action.action.text == action_name:
                action.action.click()
                break


class GridRows(UiGridRowsInterface):
    def __init__(self):
        self.rows = GridRowsFields()
        self.spinner = Field(GRID_LOADING_MASK_LOCATOR[STRATEGY_KEY], GRID_LOADING_MASK_LOCATOR[LOCATOR_KEY])

    def wait_for_spinner(self):
        assert self.spinner.is_not_visible(20) is True

    def click_row_checkbox(self, row_index: int, set_to: bool):
        checkboxes = self.rows.areas
        checkboxes[row_index].checkbox.set_to(set_to)
