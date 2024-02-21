from stere.fields import Link


class CatalogPriceRule(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class CartPriceRules(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class EmailTemplates(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class NewsletterTemplates(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class NewsletterQueue(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class NewsletterSubscribers(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class UrlRewrites(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class SearchTerms(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class SearchSynonyms(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class SiteMap(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class AllReviews(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)


class PendingReviews(Link):
    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__(strategy, locator, *args, **kwargs)
