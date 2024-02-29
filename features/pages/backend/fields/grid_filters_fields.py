from features.core_config.backend.backend_locators import (STRATEGY_KEY,
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
