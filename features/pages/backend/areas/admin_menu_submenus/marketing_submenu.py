import core_config.all as config
from stere.areas import Area
from stere.fields import Root
from pages.backend.fields.marketing_submenu_links import *

class MarketingSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(config.ADMIN_MENU_ROOT['strategy'], config.ADMIN_MENU_ROOT['locator'])
        self.catalog_price_rule = CatalogPriceRule(config.MARKETING_SUBMENU_CATALOG_PRICE_RULE_LINK_LOCATOR['strategy'], config.MARKETING_SUBMENU_CATALOG_PRICE_RULE_LINK_LOCATOR['locator'])
        self.cart_price_rules = CartPriceRules(config.MARKETING_SUBMENU_CART_PRICE_RULES_LINK_LOCATOR['strategy'], config.MARKETING_SUBMENU_CART_PRICE_RULES_LINK_LOCATOR['locator'])
        self.email_templates = EmailTemplates(config.MARKETING_SUBMENU_EMAIL_TEMPLATES_LINK_LOCATOR['strategy'], config.MARKETING_SUBMENU_EMAIL_TEMPLATES_LINK_LOCATOR['locator'])
        self.newsletter_templates = NewsletterTemplates(config.MARKETING_SUBMENU_NEWSLETTER_TEMPLATES_LINK_LOCATOR['strategy'], config.MARKETING_SUBMENU_NEWSLETTER_TEMPLATES_LINK_LOCATOR['locator'])
        self.newsletter_queue = NewsletterQueue(config.MARKETING_SUBMENU_NEWSLETTER_QUEUE_LINK_LOCATOR['strategy'], config.MARKETING_SUBMENU_NEWSLETTER_QUEUE_LINK_LOCATOR['locator'])
        self.newsletter_subscribers = NewsletterSubscribers(config.MARKETING_SUBMENU_NEWSLETTER_SUBSCIBERS_LINK_LOCATOR['strategy'], config.MARKETING_SUBMENU_NEWSLETTER_SUBSCIBERS_LINK_LOCATOR['locator'])
        self.url_rewrites = UrlRewrites(config.MARKETING_SUBMENU_URL_REWRITES_LINK_LOCATOR['strategy'], config.MARKETING_SUBMENU_URL_REWRITES_LINK_LOCATOR['locator'])
        self.search_terms = SearchTerms(config.MARKETING_SUBMENU_SEARCH_TERMS_LINK_LOCATOR['strategy'], config.MARKETING_SUBMENU_SEARCH_TERMS_LINK_LOCATOR['locator'])
        self.search_synonyms = SearchSynonyms(config.MARKETING_SUBMENU_SEARCH_SYNONYMS_LINK_LOCATOR['strategy'], config.MARKETING_SUBMENU_SEARCH_SYNONYMS_LINK_LOCATOR['locator'])
        self.site_map = SiteMap(config.MARKETING_SUBMENU_SITE_MAP_LINK_LOCATOR['strategy'], config.MARKETING_SUBMENU_SITE_MAP_LINK_LOCATOR['locator'])
        self.all_reviews = AllReviews(config.MARKETING_SUBMENU_ALL_REVIEWS_LINK_LOCATOR['strategy'], config.MARKETING_SUBMENU_ALL_REVIEWS_LINK_LOCATOR['locator'])
        self.pending_reviews = PendingReviews(config.MARKETING_SUBMENU_PENDING_REVIEWS_LINK_LOCATOR['strategy'], config.MARKETING_SUBMENU_PENDING_REVIEWS_LINK_LOCATOR['locator'])