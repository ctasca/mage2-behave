from abc import ABC, abstractmethod
from features.pages.backend.fields.grid_filters_button import GridFiltersButton
from features.pages.backend.fields.grid_fulltext_search_input import GridFulltextSearchInput
from features.pages.backend.fields.grid_fulltext_search_button import GridFulltextSearchButton
from features.pages.backend.fields.grid_apply_filters_button import GridApplyFiltersButton
from features.pages.backend.fields.grid_clear_all_filters_button import GridActiveFiltersClearAllButton
from stere.areas import Area
from stere.fields import Button, Input


class UiGridFiltersInterface(ABC):
    @abstractmethod
    def get_root(self):
        pass

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


class GridCommonFields(Area):
    FILTERS_BUTTON: str = 'filters_button'
    FULLTEXT_SEARCH_INPUT: str = 'fulltext_search_input'
    FULLTEXT_SEARCH_BUTTON: str = 'fulltext_search_button'
    APPLY_FILTERS_BUTTON: str = 'apply_filters_button'
    CLEAR_ALL_FILTERS_BUTTON: str = 'clear_all_filters_button'

    def __init__(self):
        super().__init__()
        self.filters_button = GridFiltersButton()
        self.fulltext_search_input = GridFulltextSearchInput()
        self.fulltext_search_button = GridFulltextSearchButton()
        self.apply_filters_button = GridApplyFiltersButton()
        self.clear_all_filters_button = GridActiveFiltersClearAllButton()

    def get_button(self, button_name: str) -> Button:
        """ Use the constants defined in this class to retrieve a button"""
        return getattr(self, button_name)

    def get_input(self, input_name: str) -> Input:
        """ Use the constants defined in this class to retrieve an input"""
        return getattr(self, input_name)
