import time
from stere import Stere
from typing import Optional, List
from stere.fields.decorators import use_after, use_before
from features.core_config.backend.locators.grids import (STRATEGY_KEY,
                                                         LOCATOR_KEY,
                                                         GRID_DATEPICKER_FILTER_MONTH_SELECT_LOCATOR,
                                                         GRID_DATEPICKER_FILTER_YEAR_SELECT_LOCATOR,
                                                         GRID_DATEPICKER_FILTER_DAY_LINK_LOCATOR,
                                                         GRID_DATEPICKER_GO_TO_TODAY_BUTTON_LOCATOR,
                                                         GRID_DATEPICKER_HIDE_BUTTON_LOCATOR,
                                                         GRID_DATEPICKER_TODAY_DAY_LINK_LOCATOR)
from stere.fields import Input, Button, Dropdown, Link


class InputFilter(Input):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class DatepickerFilter(Button):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)
        self.month_selector = Dropdown(
            GRID_DATEPICKER_FILTER_MONTH_SELECT_LOCATOR[STRATEGY_KEY],
            GRID_DATEPICKER_FILTER_MONTH_SELECT_LOCATOR[LOCATOR_KEY]
        )
        self.year_selector = Dropdown(
            GRID_DATEPICKER_FILTER_YEAR_SELECT_LOCATOR[STRATEGY_KEY],
            GRID_DATEPICKER_FILTER_YEAR_SELECT_LOCATOR[LOCATOR_KEY]
        )
        self.go_to_today_button = Button(GRID_DATEPICKER_GO_TO_TODAY_BUTTON_LOCATOR[STRATEGY_KEY],
                                         GRID_DATEPICKER_GO_TO_TODAY_BUTTON_LOCATOR[LOCATOR_KEY])
        self.today_day = Link(GRID_DATEPICKER_TODAY_DAY_LINK_LOCATOR[STRATEGY_KEY],
                              GRID_DATEPICKER_TODAY_DAY_LINK_LOCATOR[LOCATOR_KEY])
        self.hide_button = Button(GRID_DATEPICKER_HIDE_BUTTON_LOCATOR[STRATEGY_KEY],
                                  GRID_DATEPICKER_HIDE_BUTTON_LOCATOR[LOCATOR_KEY])

    def select_month(self, month: str) -> None:
        self.month_selector.select(month)

    def select_year(self, year: str) -> None:
        self.year_selector.select(year)

    @staticmethod
    def click_day(day: str) -> None:
        day = Link(GRID_DATEPICKER_FILTER_DAY_LINK_LOCATOR[STRATEGY_KEY],
                   GRID_DATEPICKER_FILTER_DAY_LINK_LOCATOR[LOCATOR_KEY].format(day))
        day.click()

    def go_to_today(self) -> None:
        self.go_to_today_button.click()
        self.today_day.click()

    def hide(self) -> None:
        self.hide_button.click()


class SelectFilter(Dropdown):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)

    @use_after
    @use_before
    def select(self, value: str, retry_time: Optional[int] = None) -> None:
        retry_time = retry_time or Stere.retry_time
        end_time = time.time() + retry_time

        found_options = []

        while time.time() < end_time:
            found_options = self._select(value)
            if not len(found_options):
                return

        raise ValueError(
            f'{value} was not found. Found values are: {found_options}')

    def _select(self, value: str) -> List[str]:
        found_options = []

        for option in self.options:
            found_options.append(option.html.strip())
            if option.html.strip() == value:
                option.click()
                return []

        return found_options
