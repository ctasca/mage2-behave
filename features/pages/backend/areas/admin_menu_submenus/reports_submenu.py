import core_config.all as config
from stere.areas import Area
from stere.fields import Root
from pages.backend.fields.reports_submenu_links import *

class ReportsSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(config.ADMIN_MENU_ROOT['strategy'], config.ADMIN_MENU_ROOT['locator'])
        self.products_in_cart = ProductsInCart(config.REPORTS_SUBMENU_PRODUCTS_IN_CART_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_PRODUCTS_IN_CART_LINK_LOCATOR['locator'])
        self.search_terms = SearchTerms(config.REPORTS_SUBMENU_SEARCH_TERMS_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_SEARCH_TERMS_LINK_LOCATOR['locator'])
        self.abandoned_carts = AbandonedCarts(config.REPORTS_SUBMENU_ABANDONED_CARTS_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_ABANDONED_CARTS_LINK_LOCATOR['locator'])
        self.newsletter_problem_reports = NewsletterProblemsReports(config.REPORTS_SUBMENU_NEWSLETTER_PROBLEM_REPORTS_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_NEWSLETTER_PROBLEM_REPORTS_LINK_LOCATOR['locator'])
        self.by_customers = ByCustomers(config.REPORTS_SUBMENU_BY_CUSTOMERS_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_BY_CUSTOMERS_LINK_LOCATOR['locator'])
        self.by_products = ByProducts(config.REPORTS_SUBMENU_BY_PRODUCTS_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_BY_PRODUCTS_LINK_LOCATOR['locator'])
        self.orders = Orders(config.REPORTS_SUBMENU_SALES_ORDERS_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_SALES_ORDERS_LINK_LOCATOR['locator'])
        self.tax = Tax(config.REPORTS_SUBMENU_TAX_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_TAX_LINK_LOCATOR['locator'])
        self.invoiced = Invoiced(config.REPORTS_SUBMENU_INVOICED_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_INVOICED_LINK_LOCATOR['locator'])
        self.shipping = Shipping(config.REPORTS_SUBMENU_SHIPPING_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_SHIPPING_LINK_LOCATOR['locator'])
        self.refunds = Refunds(config.REPORTS_SUBMENU_REFUNDS_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_REFUNDS_LINK_LOCATOR['locator'])
        self.coupons = Coupons(config.REPORTS_SUBMENU_COUPONS_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_COUPONS_LINK_LOCATOR['locator'])
        self.paypal_settlement = PayPalSettlement(config.REPORTS_SUBMENU_PAYPAL_SETTLEMENT_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_PAYPAL_SETTLEMENT_LINK_LOCATOR['locator'])
        self.braintree_settlement = BraintreeSettlement(config.REPORTS_SUBMENU_BRAINTREE_SETTLEMENT_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_BRAINTREE_SETTLEMENT_LINK_LOCATOR['locator'])
        self.order_total = OrderTotal(config.REPORTS_SUBMENU_ORDER_TOTAL_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_ORDER_TOTAL_LINK_LOCATOR['locator'])
        self.order_count = OrderCount(config.REPORTS_SUBMENU_ORDER_COUNT_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_ORDER_COUNT_LINK_LOCATOR['locator'])
        self.new = New(config.REPORTS_SUBMENU_NEW_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_NEW_LINK_LOCATOR['locator'])
        self.views = Views(config.REPORTS_SUBMENU_VIEWS_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_VIEWS_LINK_LOCATOR['locator'])
        self.bestsellers = Bestsellers(config.REPORTS_SUBMENU_BESTSELLERS_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_BESTSELLERS_LINK_LOCATOR['locator'])
        self.low_stock = LowStock(config.REPORTS_SUBMENU_LOW_STOCK_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_LOW_STOCK_LINK_LOCATOR['locator'])
        self.ordered = Ordered(config.REPORTS_SUBMENU_ORDERED_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_ORDERED_LINK_LOCATOR['locator'])
        self.downloads = Downloads(config.REPORTS_SUBMENU_DOWNLOADS_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_DOWNLOADS_LINK_LOCATOR['locator'])
        self.refresh_statistics = RefreshStatistics(config.REPORTS_SUBMENU_REFRESH_STATISTICS_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_REFRESH_STATISTICS_LINK_LOCATOR['locator'])
        self.advanced_reporting = AdvancedReporting(config.REPORTS_SUBMENU_ADVANCED_REPORTING_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_ADVANCED_REPORTING_LINK_LOCATOR['locator'])
        self.bi_essentials = BiEssentials(config.REPORTS_SUBMENU_BI_ESSENTIALS_LINK_LOCATOR['strategy'], config.REPORTS_SUBMENU_BI_ESSENTIALS_LINK_LOCATOR['locator'])
    
    