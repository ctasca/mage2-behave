from stere.fields import Link


class SubmenuLink(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)
