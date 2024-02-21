from features.core_config.config import *
from stere.areas import Area
from stere.fields import Root, Field


class StoreScopeList(Area):
    def __init__(self):
        super().__init__()
        self.root = Root(STORE_SCOPE_LIST_ROOT_LOCATOR['strategy'], STORE_SCOPE_LIST_ROOT_LOCATOR['locator'])
        self.store_in_scope = None

    def set_store_in_scope(self, store: str):
        store_xpath = SET_STORE_SCOPE_LOCATOR_FORMAT.format(store)
        self.store_in_scope = Field('xpath', store_xpath)
