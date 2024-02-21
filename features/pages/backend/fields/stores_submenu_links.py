from stere.fields import Link


class AllStores(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class Configuration(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class TermsAndConditions(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class OrderStatus(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class Sources(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class Stocks(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class TaxRules(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class TaxZonesAndRates(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class CurrencyRates(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class CurrencySymbols(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class Product(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class AttributeSet(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class Rating(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)
