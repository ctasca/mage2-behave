import time

import features.core_config.all as config
from stere.areas import Area
from stere.fields import Button, Root, Field


class StoreChangeButton(Button):
    def __init__(self):
        super().__init__(config.STORE_CHANGE_BUTTON_LINK_LOCATOR['strategy'],
                         config.STORE_CHANGE_BUTTON_LINK_LOCATOR['locator'])

    def switch_to_store(self, store_name: str) -> None:
        self.click()
        store_xpath = "//a[contains(text(), '{}')]".format(store_name)
        store_selector = Area(
            root=Root('xpath', "//ul[@data-role='stores-list']"),
            desired_store=Field('xpath', store_xpath)
        )
        store_selector.desired_store.click()
