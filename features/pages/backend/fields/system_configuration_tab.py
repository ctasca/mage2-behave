from stere.fields import Field


class SystemConfigurationTab(Field):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)
