from stere.fields import Link


class Orders(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class Invoices(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class Shipments(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class CreditMemos(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class BillingAgreements(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class Transactions(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class BraintreeVirualTerminal(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)
