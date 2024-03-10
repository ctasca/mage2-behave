from features.core_config.backend.locators.admin_menu import ADMIN_MENU_ROOT
from features.core_config.backend.locators.admin_submenus import *
from stere.areas import Area
from stere.fields import Root, Link
from features.pages.backend.fields.submenu_link import SubmenuLink
from typing import List
from features.core_config.strategies import STRATEGY_KEY, LOCATOR_KEY


class ReportsSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(ADMIN_MENU_ROOT[STRATEGY_KEY], ADMIN_MENU_ROOT[LOCATOR_KEY])
        self.products_in_cart = SubmenuLink(REPORTS_SUBMENU_PRODUCTS_IN_CART_LINK_LOCATOR[STRATEGY_KEY],
                                            REPORTS_SUBMENU_PRODUCTS_IN_CART_LINK_LOCATOR[LOCATOR_KEY])
        self.search_terms = SubmenuLink(REPORTS_SUBMENU_SEARCH_TERMS_LINK_LOCATOR[STRATEGY_KEY],
                                        REPORTS_SUBMENU_SEARCH_TERMS_LINK_LOCATOR[LOCATOR_KEY])
        self.abandoned_carts = SubmenuLink(REPORTS_SUBMENU_ABANDONED_CARTS_LINK_LOCATOR[STRATEGY_KEY],
                                           REPORTS_SUBMENU_ABANDONED_CARTS_LINK_LOCATOR[LOCATOR_KEY])
        self.newsletter_problem_reports = SubmenuLink(
            REPORTS_SUBMENU_NEWSLETTER_PROBLEM_REPORTS_LINK_LOCATOR[STRATEGY_KEY],
            REPORTS_SUBMENU_NEWSLETTER_PROBLEM_REPORTS_LINK_LOCATOR[LOCATOR_KEY])
        self.by_customers = SubmenuLink(REPORTS_SUBMENU_BY_CUSTOMERS_LINK_LOCATOR[STRATEGY_KEY],
                                        REPORTS_SUBMENU_BY_CUSTOMERS_LINK_LOCATOR[LOCATOR_KEY])
        self.by_products = SubmenuLink(REPORTS_SUBMENU_BY_PRODUCTS_LINK_LOCATOR[STRATEGY_KEY],
                                       REPORTS_SUBMENU_BY_PRODUCTS_LINK_LOCATOR[LOCATOR_KEY])
        self.orders = SubmenuLink(REPORTS_SUBMENU_SALES_ORDERS_LINK_LOCATOR[STRATEGY_KEY],
                                  REPORTS_SUBMENU_SALES_ORDERS_LINK_LOCATOR[LOCATOR_KEY])
        self.tax = SubmenuLink(REPORTS_SUBMENU_TAX_LINK_LOCATOR[STRATEGY_KEY],
                               REPORTS_SUBMENU_TAX_LINK_LOCATOR[LOCATOR_KEY])
        self.invoiced = SubmenuLink(REPORTS_SUBMENU_INVOICED_LINK_LOCATOR[STRATEGY_KEY],
                                    REPORTS_SUBMENU_INVOICED_LINK_LOCATOR[LOCATOR_KEY])
        self.shipping = SubmenuLink(REPORTS_SUBMENU_SHIPPING_LINK_LOCATOR[STRATEGY_KEY],
                                    REPORTS_SUBMENU_SHIPPING_LINK_LOCATOR[LOCATOR_KEY])
        self.refunds = SubmenuLink(REPORTS_SUBMENU_REFUNDS_LINK_LOCATOR[STRATEGY_KEY],
                                   REPORTS_SUBMENU_REFUNDS_LINK_LOCATOR[LOCATOR_KEY])
        self.coupons = SubmenuLink(REPORTS_SUBMENU_COUPONS_LINK_LOCATOR[STRATEGY_KEY],
                                   REPORTS_SUBMENU_COUPONS_LINK_LOCATOR[LOCATOR_KEY])
        self.paypal_settlement = SubmenuLink(REPORTS_SUBMENU_PAYPAL_SETTLEMENT_LINK_LOCATOR[STRATEGY_KEY],
                                             REPORTS_SUBMENU_PAYPAL_SETTLEMENT_LINK_LOCATOR[LOCATOR_KEY])
        self.braintree_settlement = SubmenuLink(
            REPORTS_SUBMENU_BRAINTREE_SETTLEMENT_LINK_LOCATOR[STRATEGY_KEY],
            REPORTS_SUBMENU_BRAINTREE_SETTLEMENT_LINK_LOCATOR[LOCATOR_KEY])
        self.order_total = SubmenuLink(REPORTS_SUBMENU_ORDER_TOTAL_LINK_LOCATOR[STRATEGY_KEY],
                                       REPORTS_SUBMENU_ORDER_TOTAL_LINK_LOCATOR[LOCATOR_KEY])
        self.order_count = SubmenuLink(REPORTS_SUBMENU_ORDER_COUNT_LINK_LOCATOR[STRATEGY_KEY],
                                       REPORTS_SUBMENU_ORDER_COUNT_LINK_LOCATOR[LOCATOR_KEY])
        self.new = SubmenuLink(REPORTS_SUBMENU_NEW_LINK_LOCATOR[STRATEGY_KEY],
                               REPORTS_SUBMENU_NEW_LINK_LOCATOR[LOCATOR_KEY])
        self.views = SubmenuLink(REPORTS_SUBMENU_VIEWS_LINK_LOCATOR[STRATEGY_KEY],
                                 REPORTS_SUBMENU_VIEWS_LINK_LOCATOR[LOCATOR_KEY])
        self.bestsellers = SubmenuLink(REPORTS_SUBMENU_BESTSELLERS_LINK_LOCATOR[STRATEGY_KEY],
                                       REPORTS_SUBMENU_BESTSELLERS_LINK_LOCATOR[LOCATOR_KEY])
        self.low_stock = SubmenuLink(REPORTS_SUBMENU_LOW_STOCK_LINK_LOCATOR[STRATEGY_KEY],
                                     REPORTS_SUBMENU_LOW_STOCK_LINK_LOCATOR[LOCATOR_KEY])
        self.ordered = SubmenuLink(REPORTS_SUBMENU_ORDERED_LINK_LOCATOR[STRATEGY_KEY],
                                   REPORTS_SUBMENU_ORDERED_LINK_LOCATOR[LOCATOR_KEY])
        self.downloads = SubmenuLink(REPORTS_SUBMENU_DOWNLOADS_LINK_LOCATOR[STRATEGY_KEY],
                                     REPORTS_SUBMENU_DOWNLOADS_LINK_LOCATOR[LOCATOR_KEY])
        self.refresh_statistics = SubmenuLink(REPORTS_SUBMENU_REFRESH_STATISTICS_LINK_LOCATOR[STRATEGY_KEY],
                                              REPORTS_SUBMENU_REFRESH_STATISTICS_LINK_LOCATOR[LOCATOR_KEY])
        self.advanced_reporting = SubmenuLink(REPORTS_SUBMENU_ADVANCED_REPORTING_LINK_LOCATOR[STRATEGY_KEY],
                                              REPORTS_SUBMENU_ADVANCED_REPORTING_LINK_LOCATOR[LOCATOR_KEY])
        self.bi_essentials = SubmenuLink(REPORTS_SUBMENU_BI_ESSENTIALS_LINK_LOCATOR[STRATEGY_KEY],
                                         REPORTS_SUBMENU_BI_ESSENTIALS_LINK_LOCATOR[LOCATOR_KEY])

    def links(self) -> List[Link]:
        return [
            self.products_in_cart,
            self.search_terms,
            self.abandoned_carts,
            self.newsletter_problem_reports,
            self.by_customers,
            self.by_products,
            self.orders,
            self.tax,
            self.invoiced,
            self.shipping,
            self.refunds,
            self.coupons,
            self.paypal_settlement,
            self.braintree_settlement,
            self.order_total,
            self.order_count,
            self.new,
            self.views,
            self.bestsellers,
            self.low_stock,
            self.ordered,
            self.downloads,
            self.refresh_statistics,
            self.advanced_reporting,
            self.bi_essentials
        ]
