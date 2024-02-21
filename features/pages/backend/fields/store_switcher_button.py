import features.core_config.config as config
from stere.fields import Button
from features.pages.backend.areas.store_scope_list import StoreScopeList


class StoreSwitcher(Button):
    def __init__(self):
        super().__init__(config.STORE_CHANGE_BUTTON_LINK_LOCATOR['strategy'],
                         config.STORE_CHANGE_BUTTON_LINK_LOCATOR['locator'])

    def switch_to_store(self, store_name: str) -> None:
        self.click()
        store_scope_list = StoreScopeList()
        store_scope_list.set_store_in_scope(store_name)
        store_scope_list.store_in_scope.click()
