from features.core_config.backend.backend_locators import *
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.reports_submenu_links import *
from typing import List


class ReportsSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(ADMIN_MENU_ROOT['strategy'], ADMIN_MENU_ROOT['locator'])
        self.products_in_cart = ProductsInCart(REPORTS_SUBMENU_PRODUCTS_IN_CART_LINK_LOCATOR['strategy'],
                                               REPORTS_SUBMENU_PRODUCTS_IN_CART_LINK_LOCATOR['locator'])
        self.search_terms = SearchTerms(REPORTS_SUBMENU_SEARCH_TERMS_LINK_LOCATOR['strategy'],
                                        REPORTS_SUBMENU_SEARCH_TERMS_LINK_LOCATOR['locator'])
        self.abandoned_carts = AbandonedCarts(REPORTS_SUBMENU_ABANDONED_CARTS_LINK_LOCATOR['strategy'],
                                              REPORTS_SUBMENU_ABANDONED_CARTS_LINK_LOCATOR['locator'])
        self.newsletter_problem_reports = NewsletterProblemsReports(
            REPORTS_SUBMENU_NEWSLETTER_PROBLEM_REPORTS_LINK_LOCATOR['strategy'],
            REPORTS_SUBMENU_NEWSLETTER_PROBLEM_REPORTS_LINK_LOCATOR['locator'])
        self.by_customers = ByCustomers(REPORTS_SUBMENU_BY_CUSTOMERS_LINK_LOCATOR['strategy'],
                                        REPORTS_SUBMENU_BY_CUSTOMERS_LINK_LOCATOR['locator'])
        self.by_products = ByProducts(REPORTS_SUBMENU_BY_PRODUCTS_LINK_LOCATOR['strategy'],
                                      REPORTS_SUBMENU_BY_PRODUCTS_LINK_LOCATOR['locator'])
        self.orders = Orders(REPORTS_SUBMENU_SALES_ORDERS_LINK_LOCATOR['strategy'],
                             REPORTS_SUBMENU_SALES_ORDERS_LINK_LOCATOR['locator'])
        self.tax = Tax(REPORTS_SUBMENU_TAX_LINK_LOCATOR['strategy'],
                       REPORTS_SUBMENU_TAX_LINK_LOCATOR['locator'])
        self.invoiced = Invoiced(REPORTS_SUBMENU_INVOICED_LINK_LOCATOR['strategy'],
                                 REPORTS_SUBMENU_INVOICED_LINK_LOCATOR['locator'])
        self.shipping = Shipping(REPORTS_SUBMENU_SHIPPING_LINK_LOCATOR['strategy'],
                                 REPORTS_SUBMENU_SHIPPING_LINK_LOCATOR['locator'])
        self.refunds = Refunds(REPORTS_SUBMENU_REFUNDS_LINK_LOCATOR['strategy'],
                               REPORTS_SUBMENU_REFUNDS_LINK_LOCATOR['locator'])
        self.coupons = Coupons(REPORTS_SUBMENU_COUPONS_LINK_LOCATOR['strategy'],
                               REPORTS_SUBMENU_COUPONS_LINK_LOCATOR['locator'])
        self.paypal_settlement = PayPalSettlement(REPORTS_SUBMENU_PAYPAL_SETTLEMENT_LINK_LOCATOR['strategy'],
                                                  REPORTS_SUBMENU_PAYPAL_SETTLEMENT_LINK_LOCATOR['locator'])
        self.braintree_settlement = BraintreeSettlement(
            REPORTS_SUBMENU_BRAINTREE_SETTLEMENT_LINK_LOCATOR['strategy'],
            REPORTS_SUBMENU_BRAINTREE_SETTLEMENT_LINK_LOCATOR['locator'])
        self.order_total = OrderTotal(REPORTS_SUBMENU_ORDER_TOTAL_LINK_LOCATOR['strategy'],
                                      REPORTS_SUBMENU_ORDER_TOTAL_LINK_LOCATOR['locator'])
        self.order_count = OrderCount(REPORTS_SUBMENU_ORDER_COUNT_LINK_LOCATOR['strategy'],
                                      REPORTS_SUBMENU_ORDER_COUNT_LINK_LOCATOR['locator'])
        self.new = New(REPORTS_SUBMENU_NEW_LINK_LOCATOR['strategy'],
                       REPORTS_SUBMENU_NEW_LINK_LOCATOR['locator'])
        self.views = Views(REPORTS_SUBMENU_VIEWS_LINK_LOCATOR['strategy'],
                           REPORTS_SUBMENU_VIEWS_LINK_LOCATOR['locator'])
        self.bestsellers = Bestsellers(REPORTS_SUBMENU_BESTSELLERS_LINK_LOCATOR['strategy'],
                                       REPORTS_SUBMENU_BESTSELLERS_LINK_LOCATOR['locator'])
        self.low_stock = LowStock(REPORTS_SUBMENU_LOW_STOCK_LINK_LOCATOR['strategy'],
                                  REPORTS_SUBMENU_LOW_STOCK_LINK_LOCATOR['locator'])
        self.ordered = Ordered(REPORTS_SUBMENU_ORDERED_LINK_LOCATOR['strategy'],
                               REPORTS_SUBMENU_ORDERED_LINK_LOCATOR['locator'])
        self.downloads = Downloads(REPORTS_SUBMENU_DOWNLOADS_LINK_LOCATOR['strategy'],
                                   REPORTS_SUBMENU_DOWNLOADS_LINK_LOCATOR['locator'])
        self.refresh_statistics = RefreshStatistics(REPORTS_SUBMENU_REFRESH_STATISTICS_LINK_LOCATOR['strategy'],
                                                    REPORTS_SUBMENU_REFRESH_STATISTICS_LINK_LOCATOR['locator'])
        self.advanced_reporting = AdvancedReporting(REPORTS_SUBMENU_ADVANCED_REPORTING_LINK_LOCATOR['strategy'],
                                                    REPORTS_SUBMENU_ADVANCED_REPORTING_LINK_LOCATOR['locator'])
        self.bi_essentials = BiEssentials(REPORTS_SUBMENU_BI_ESSENTIALS_LINK_LOCATOR['strategy'],
                                          REPORTS_SUBMENU_BI_ESSENTIALS_LINK_LOCATOR['locator'])

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
