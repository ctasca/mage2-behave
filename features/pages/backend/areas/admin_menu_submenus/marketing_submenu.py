import features.core_config.backend.backend_locators as bl
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.marketing_submenu_links import *
from typing import List


class MarketingSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.ADMIN_MENU_ROOT[STRATEGY_KEY], bl.ADMIN_MENU_ROOT[LOCATOR_KEY])
        self.catalog_price_rule = CatalogPriceRule(bl.MARKETING_SUBMENU_CATALOG_PRICE_RULE_LINK_LOCATOR[STRATEGY_KEY],
                                                   bl.MARKETING_SUBMENU_CATALOG_PRICE_RULE_LINK_LOCATOR[LOCATOR_KEY])
        self.cart_price_rules = CartPriceRules(bl.MARKETING_SUBMENU_CART_PRICE_RULES_LINK_LOCATOR[STRATEGY_KEY],
                                               bl.MARKETING_SUBMENU_CART_PRICE_RULES_LINK_LOCATOR[LOCATOR_KEY])
        self.email_templates = EmailTemplates(bl.MARKETING_SUBMENU_EMAIL_TEMPLATES_LINK_LOCATOR[STRATEGY_KEY],
                                              bl.MARKETING_SUBMENU_EMAIL_TEMPLATES_LINK_LOCATOR[LOCATOR_KEY])
        self.newsletter_templates = NewsletterTemplates(
            bl.MARKETING_SUBMENU_NEWSLETTER_TEMPLATES_LINK_LOCATOR[STRATEGY_KEY],
            bl.MARKETING_SUBMENU_NEWSLETTER_TEMPLATES_LINK_LOCATOR[LOCATOR_KEY])
        self.newsletter_queue = NewsletterQueue(bl.MARKETING_SUBMENU_NEWSLETTER_QUEUE_LINK_LOCATOR[STRATEGY_KEY],
                                                bl.MARKETING_SUBMENU_NEWSLETTER_QUEUE_LINK_LOCATOR[LOCATOR_KEY])
        self.newsletter_subscribers = NewsletterSubscribers(
            bl.MARKETING_SUBMENU_NEWSLETTER_SUBSCIBERS_LINK_LOCATOR[STRATEGY_KEY],
            bl.MARKETING_SUBMENU_NEWSLETTER_SUBSCIBERS_LINK_LOCATOR[LOCATOR_KEY])
        self.url_rewrites = UrlRewrites(bl.MARKETING_SUBMENU_URL_REWRITES_LINK_LOCATOR[STRATEGY_KEY],
                                        bl.MARKETING_SUBMENU_URL_REWRITES_LINK_LOCATOR[LOCATOR_KEY])
        self.search_terms = SearchTerms(bl.MARKETING_SUBMENU_SEARCH_TERMS_LINK_LOCATOR[STRATEGY_KEY],
                                        bl.MARKETING_SUBMENU_SEARCH_TERMS_LINK_LOCATOR[LOCATOR_KEY])
        self.search_synonyms = SearchSynonyms(bl.MARKETING_SUBMENU_SEARCH_SYNONYMS_LINK_LOCATOR[STRATEGY_KEY],
                                              bl.MARKETING_SUBMENU_SEARCH_SYNONYMS_LINK_LOCATOR[LOCATOR_KEY])
        self.site_map = SiteMap(bl.MARKETING_SUBMENU_SITE_MAP_LINK_LOCATOR[STRATEGY_KEY],
                                bl.MARKETING_SUBMENU_SITE_MAP_LINK_LOCATOR[LOCATOR_KEY])
        self.all_reviews = AllReviews(bl.MARKETING_SUBMENU_ALL_REVIEWS_LINK_LOCATOR[STRATEGY_KEY],
                                      bl.MARKETING_SUBMENU_ALL_REVIEWS_LINK_LOCATOR[LOCATOR_KEY])
        self.pending_reviews = PendingReviews(bl.MARKETING_SUBMENU_PENDING_REVIEWS_LINK_LOCATOR[STRATEGY_KEY],
                                              bl.MARKETING_SUBMENU_PENDING_REVIEWS_LINK_LOCATOR[LOCATOR_KEY])

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
