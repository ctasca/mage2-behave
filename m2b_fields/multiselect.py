import platform
from typing import List
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from stere.fields import Dropdown


class MultiSelectField(Dropdown):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.multiple = True

    def multiselect(self, context, options_to_select: List[str], *args, **kwargs):
        os_name = platform.system()
        actions = ActionChains(context.browser.driver)
        for option in self.options:
            if option.text.strip() in options_to_select:
                actions.key_down(Keys.COMMAND if os_name == 'Darwin' else Keys.CONTROL) \
                    .click(option._element) \
                    .key_up(Keys.COMMAND if os_name == 'Darwin' else Keys.CONTROL)
        actions.perform()
