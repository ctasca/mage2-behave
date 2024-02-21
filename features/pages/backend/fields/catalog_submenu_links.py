from stere.fields import Link


class Products(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class Categories(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)
