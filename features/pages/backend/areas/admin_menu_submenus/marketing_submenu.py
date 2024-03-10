from features.core_config.backend.locators.admin_menu import ADMIN_MENU_ROOT
from features.core_config.backend.locators.admin_submenus import *
from features.core_config.strategies import STRATEGY_KEY, LOCATOR_KEY
from stere.areas import Area
from stere.fields import Root, Link
from features.pages.backend.fields.submenu_link import SubmenuLink
from typing import List


class MarketingSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(ADMIN_MENU_ROOT[STRATEGY_KEY], ADMIN_MENU_ROOT[LOCATOR_KEY])
        self.catalog_price_rule = SubmenuLink(MARKETING_SUBMENU_CATALOG_PRICE_RULE_LINK_LOCATOR[STRATEGY_KEY],
                                              MARKETING_SUBMENU_CATALOG_PRICE_RULE_LINK_LOCATOR[LOCATOR_KEY])
        self.cart_price_rules = SubmenuLink(MARKETING_SUBMENU_CART_PRICE_RULES_LINK_LOCATOR[STRATEGY_KEY],
                                            MARKETING_SUBMENU_CART_PRICE_RULES_LINK_LOCATOR[LOCATOR_KEY])
        self.email_templates = SubmenuLink(MARKETING_SUBMENU_EMAIL_TEMPLATES_LINK_LOCATOR[STRATEGY_KEY],
                                           MARKETING_SUBMENU_EMAIL_TEMPLATES_LINK_LOCATOR[LOCATOR_KEY])
        self.newsletter_templates = SubmenuLink(
            MARKETING_SUBMENU_NEWSLETTER_TEMPLATES_LINK_LOCATOR[STRATEGY_KEY],
            MARKETING_SUBMENU_NEWSLETTER_TEMPLATES_LINK_LOCATOR[LOCATOR_KEY])
        self.newsletter_queue = SubmenuLink(MARKETING_SUBMENU_NEWSLETTER_QUEUE_LINK_LOCATOR[STRATEGY_KEY],
                                            MARKETING_SUBMENU_NEWSLETTER_QUEUE_LINK_LOCATOR[LOCATOR_KEY])
        self.newsletter_subscribers = SubmenuLink(
            MARKETING_SUBMENU_NEWSLETTER_SUBSCIBERS_LINK_LOCATOR[STRATEGY_KEY],
            MARKETING_SUBMENU_NEWSLETTER_SUBSCIBERS_LINK_LOCATOR[LOCATOR_KEY])
        self.url_rewrites = SubmenuLink(MARKETING_SUBMENU_URL_REWRITES_LINK_LOCATOR[STRATEGY_KEY],
                                        MARKETING_SUBMENU_URL_REWRITES_LINK_LOCATOR[LOCATOR_KEY])
        self.search_terms = SubmenuLink(MARKETING_SUBMENU_SEARCH_TERMS_LINK_LOCATOR[STRATEGY_KEY],
                                        MARKETING_SUBMENU_SEARCH_TERMS_LINK_LOCATOR[LOCATOR_KEY])
        self.search_synonyms = SubmenuLink(MARKETING_SUBMENU_SEARCH_SYNONYMS_LINK_LOCATOR[STRATEGY_KEY],
                                           MARKETING_SUBMENU_SEARCH_SYNONYMS_LINK_LOCATOR[LOCATOR_KEY])
        self.site_map = SubmenuLink(MARKETING_SUBMENU_SITE_MAP_LINK_LOCATOR[STRATEGY_KEY],
                                    MARKETING_SUBMENU_SITE_MAP_LINK_LOCATOR[LOCATOR_KEY])
        self.all_reviews = SubmenuLink(MARKETING_SUBMENU_ALL_REVIEWS_LINK_LOCATOR[STRATEGY_KEY],
                                       MARKETING_SUBMENU_ALL_REVIEWS_LINK_LOCATOR[LOCATOR_KEY])
        self.pending_reviews = SubmenuLink(MARKETING_SUBMENU_PENDING_REVIEWS_LINK_LOCATOR[STRATEGY_KEY],
                                           MARKETING_SUBMENU_PENDING_REVIEWS_LINK_LOCATOR[LOCATOR_KEY])

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
