from abc import ABC, abstractmethod
from features.pages.backend.fields.grid_filters_button import GridFiltersButton
from features.pages.backend.fields.grid_fulltext_search_input import GridFulltextSearchInput
from features.pages.backend.fields.grid_fulltext_search_button import GridFulltextSearchButton
from features.pages.backend.fields.grid_apply_filters_button import GridApplyFiltersButton
from features.pages.backend.fields.grid_clear_all_filters_button import GridActiveFiltersClearAllButton
from features.pages.backend.fields.grid_actions_fields import GridActionsButton


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


class GridCommonFiltersFields:
    def __init__(self):
        self.filters_button = GridFiltersButton()
        self.fulltext_search_input = GridFulltextSearchInput()
        self.fulltext_search_button = GridFulltextSearchButton()
        self.apply_filters_button = GridApplyFiltersButton()
        self.clear_all_filters_button = GridActiveFiltersClearAllButton()


class GridCommonActionsFields:
    def __init__(self):
        self.actions_button = GridActionsButton()
