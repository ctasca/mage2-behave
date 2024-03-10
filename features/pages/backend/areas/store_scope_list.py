from features.core_config.backend.locators.store_scopes import *
from stere.areas import Area
from stere.fields import Root, Field


class StoreScopeList(Area):
    def __init__(self):
        super().__init__()
        self.root = Root(STORE_SCOPE_LIST_ROOT_LOCATOR[STRATEGY_KEY], STORE_SCOPE_LIST_ROOT_LOCATOR[LOCATOR_KEY])
        self.store_in_scope = None

    def set_store_in_scope(self, store: str):
        store_xpath = SET_STORE_SCOPE_LOCATOR_FORMAT.format(store)
        self.store_in_scope = Field(XPATH_STRATEGY, store_xpath)
