from features.core_config.backend.backend_locators import *
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.marketing_submenu_links import *
from typing import List


class MarketingSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(ADMIN_MENU_ROOT['strategy'], ADMIN_MENU_ROOT['locator'])
        self.catalog_price_rule = CatalogPriceRule(MARKETING_SUBMENU_CATALOG_PRICE_RULE_LINK_LOCATOR['strategy'],
                                                   MARKETING_SUBMENU_CATALOG_PRICE_RULE_LINK_LOCATOR['locator'])
        self.cart_price_rules = CartPriceRules(MARKETING_SUBMENU_CART_PRICE_RULES_LINK_LOCATOR['strategy'],
                                               MARKETING_SUBMENU_CART_PRICE_RULES_LINK_LOCATOR['locator'])
        self.email_templates = EmailTemplates(MARKETING_SUBMENU_EMAIL_TEMPLATES_LINK_LOCATOR['strategy'],
                                              MARKETING_SUBMENU_EMAIL_TEMPLATES_LINK_LOCATOR['locator'])
        self.newsletter_templates = NewsletterTemplates(
            MARKETING_SUBMENU_NEWSLETTER_TEMPLATES_LINK_LOCATOR['strategy'],
            MARKETING_SUBMENU_NEWSLETTER_TEMPLATES_LINK_LOCATOR['locator'])
        self.newsletter_queue = NewsletterQueue(MARKETING_SUBMENU_NEWSLETTER_QUEUE_LINK_LOCATOR['strategy'],
                                                MARKETING_SUBMENU_NEWSLETTER_QUEUE_LINK_LOCATOR['locator'])
        self.newsletter_subscribers = NewsletterSubscribers(
            MARKETING_SUBMENU_NEWSLETTER_SUBSCIBERS_LINK_LOCATOR['strategy'],
            MARKETING_SUBMENU_NEWSLETTER_SUBSCIBERS_LINK_LOCATOR['locator'])
        self.url_rewrites = UrlRewrites(MARKETING_SUBMENU_URL_REWRITES_LINK_LOCATOR['strategy'],
                                        MARKETING_SUBMENU_URL_REWRITES_LINK_LOCATOR['locator'])
        self.search_terms = SearchTerms(MARKETING_SUBMENU_SEARCH_TERMS_LINK_LOCATOR['strategy'],
                                        MARKETING_SUBMENU_SEARCH_TERMS_LINK_LOCATOR['locator'])
        self.search_synonyms = SearchSynonyms(MARKETING_SUBMENU_SEARCH_SYNONYMS_LINK_LOCATOR['strategy'],
                                              MARKETING_SUBMENU_SEARCH_SYNONYMS_LINK_LOCATOR['locator'])
        self.site_map = SiteMap(MARKETING_SUBMENU_SITE_MAP_LINK_LOCATOR['strategy'],
                                MARKETING_SUBMENU_SITE_MAP_LINK_LOCATOR['locator'])
        self.all_reviews = AllReviews(MARKETING_SUBMENU_ALL_REVIEWS_LINK_LOCATOR['strategy'],
                                      MARKETING_SUBMENU_ALL_REVIEWS_LINK_LOCATOR['locator'])
        self.pending_reviews = PendingReviews(MARKETING_SUBMENU_PENDING_REVIEWS_LINK_LOCATOR['strategy'],
                                              MARKETING_SUBMENU_PENDING_REVIEWS_LINK_LOCATOR['locator'])

    def links(self) -> List[Link]:
        return [
            self.catalog_price_rule,
            self.cart_price_rules,
            self.email_templates,
            self.newsletter_templates,
            self.newsletter_queue,
            self.newsletter_subscribers,
            self.url_rewrites,
            self.search_terms,
            self.search_synonyms,
            self.site_map,
            self.all_reviews,
            self.pending_reviews
        ]
