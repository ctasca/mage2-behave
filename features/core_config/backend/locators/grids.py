from typing import Dict

from features.core_config.strategies import STRATEGY_KEY, XPATH_STRATEGY, LOCATOR_KEY, ID_STRATEGY

GRID_FILTER_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "(//div[@class=\"data-grid-filters-action-wrap\"]//button["
                                                "@data-action=\"grid-filter-expand\"])[1]"}
GRID_FULLTEXT_INPUT_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "fulltext"}
GRID_FULLTEXT_SEARCH_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "(//div[@class='data-grid-search-control-wrap']/button)[1]"}
GRID_ACTIVE_FILTERS_ROOT_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: '(//ul[@data-role="filter-list"]//li)[1]'}
GRID_ACTIVE_FILERS_BUTTON_LOCATOR: Dict[str, str] = {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: './button'}
GRID_APPLY_FILTERS_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//button[@data-action='grid-filter-apply']"}
GRID_FILTERS_ROOT_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: '//div[@data-part="filter-form"]'}
GRID_DATEPICKER_BUTTON_LOCATOR: Dict[str, str] = {STRATEGY_KEY: XPATH_STRATEGY,
                                                  LOCATOR_KEY: "//input[@name='{}']//following-sibling::button["
                                                               "contains(@class, 'ui-datepicker-trigger')]"}
GRID_DATEPICKER_FILTER_MONTH_SELECT_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//select[@class='ui-datepicker-month']"}
GRID_DATEPICKER_FILTER_YEAR_SELECT_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//select[@class='ui-datepicker-year']"}
GRID_DATEPICKER_FILTER_DAY_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//a[@data-date='{}']"}
GRID_DATEPICKER_GO_TO_TODAY_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//button[@data-handler='today']"}
GRID_DATEPICKER_TODAY_DAY_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//a[contains(@class, 'ui-state-default ui-state-active')]"}
GRID_DATEPICKER_HIDE_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//button[@data-handler='hide']"}
GRID_CLEAR_ALL_FILTERS_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "(//button[@data-action=\"grid-filter-reset\"])[1]"}
GRID_ACTIONS_BUTTON_LOCATOR: Dict[str, str] = {
    STRATEGY_KEY: XPATH_STRATEGY,
    LOCATOR_KEY: "(//button[@data-bind=\"attr: {title: $t('Select Items')}, click: toggleOpened\"])[1]"}
GRID_ACTIONS_LIST_ROOT_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "(//ul[@class='action-menu _active'])[1]/li"}
GRID_ACTION_XPATH_LOCATOR: str = "./span"
GRID_ACTIONS_SUBMENU_ROOT_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: '(//ul[@class="action-submenu _active"])[1]/li'}
GRID_ACTIONS_SUBMENU_XPATH_LOCATOR: str = "./span"
GRID_ROWS_ROOT_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//main[@id='anchor-content']//table[@data-role='grid']/tbody/tr"}
GRID_ROW_CHECKBOX_LOCATOR: str = "./td[1]/label/input[@data-action='select-row']"
GRID_LOADING_MASK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY,
     LOCATOR_KEY: "//main[@id='anchor-content']//div[@class='admin__data-grid-loading-mask']"}
