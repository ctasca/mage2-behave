from typing import Dict

ADMIN_LOGIN_FORM_USERNAME_LOCATOR: Dict[str, str] = {"strategy": "id", "locator": "username"}
ADMIN_LOGIN_FORM_PASSWORD_LOCATOR: Dict[str, str] = {"strategy": "id", "locator": "login"}
ADMIN_LOGIN_FORM_SIGNIN_BUTTON_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".action-login.action-primary"}
# Admin menu
ADMIN_MENU_ROOT: Dict[str, str] = {"strategy": "id", "locator": "nav"}
ADMIN_MENU_DASHBOARD_LINK_LOCATOR: Dict[str, str] = {"strategy": "id", "locator": "menu-magento-backend-dashboard"}
ADMIN_MENU_SALES_LINK_LOCATOR: Dict[str, str] = {"strategy": "id", "locator": "menu-magento-sales-sales"}
ADMIN_MENU_CATALOG_LINK_LOCATOR: Dict[str, str] = {"strategy": "id", "locator": "menu-magento-catalog-catalog"}
ADMIN_MENU_CUSTOMERS_LINK_LOCATOR: Dict[str, str] = {"strategy": "id", "locator": "menu-magento-customer-customer"}
ADMIN_MENU_MARKETING_LINK_LOCATOR: Dict[str, str] = {"strategy": "id", "locator": "menu-magento-backend-marketing"}
ADMIN_MENU_CONTENT_LINK_LOCATOR: Dict[str, str] = {"strategy": "id", "locator": "menu-magento-backend-content"}
ADMIN_MENU_REPORTS_LINK_LOCATOR: Dict[str, str] = {"strategy": "id", "locator": "menu-magento-reports-report"}
ADMIN_MENU_STORES_LINK_LOCATOR: Dict[str, str] = {"strategy": "id", "locator": "menu-magento-backend-stores"}
ADMIN_MENU_SYSTEM_LINK_LOCATOR: Dict[str, str] = {"strategy": "id", "locator": "menu-magento-backend-system"}
# Admin menu submenus
SALES_SUBMENU_ORDERS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-sales-order"}
SALES_SUBMENU_INVOICES_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-sales-order"}
SALES_SUBMENU_SHIPMENTS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-sales-shipment"}
SALES_SUBMENU_CREDITMEMOS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-sales-creditmemo"}
SALES_SUBMENU_BILLING_AGREEMENTS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-paypal-billing-agreement"}
SALES_SUBMENU_TRANSACTIONS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-sales-transactions"}
SALES_SUBMENU_VIRTUAL_TERMINAL_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-virtual-terminal"}
CATALOG_SUBMENU_PRODUCTS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-catalog-products"}
CATALOG_SUBMENU_CATEGORIES_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-catalog-categories"}
CUSTOMERS_SUBMENU_ALL_CUSTOMERS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-customer-manage"}
CUSTOMERS_SUBMENU_ONLINE_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-customer-online"}
CUSTOMERS_SUBMENU_AS_CUSTOMER_LOG_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-login-log"}
CUSTOMERS_SUBMENU_GROUPS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-customer-group"}
MARKETING_SUBMENU_CATALOG_PRICE_RULE_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-promo-catalog"}
MARKETING_SUBMENU_CART_PRICE_RULES_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-promo-quote"}
MARKETING_SUBMENU_EMAIL_TEMPLATES_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-template"}
MARKETING_SUBMENU_NEWSLETTER_TEMPLATES_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-newsletter-template"}
MARKETING_SUBMENU_NEWSLETTER_QUEUE_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-newsletter-queue"}
MARKETING_SUBMENU_NEWSLETTER_SUBSCIBERS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-newsletter-subscriber"}
MARKETING_SUBMENU_URL_REWRITES_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-urlrewrite"}
MARKETING_SUBMENU_SEARCH_TERMS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-search-terms"}
MARKETING_SUBMENU_SEARCH_SYNONYMS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-search-synonyms"}
MARKETING_SUBMENU_SITE_MAP_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-catalog-sitemap"}
MARKETING_SUBMENU_ALL_REVIEWS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-catalog-reviews-ratings-reviews-all"}
MARKETING_SUBMENU_PENDING_REVIEWS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-catalog-reviews-ratings-pending"}
CONTENT_SUBMENU_PAGES_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-cms-page"}
CONTENT_SUBMENU_BLOCKS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-cms-block"}
CONTENT_SUBMENU_WIDGETS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-cms-widget-instance"}
CONTENT_SUBMENU_TEMPLATES_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-templates"}
CONTENT_SUBMENU_MEDIA_GALLERY_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-media-gallery"}
CONTENT_SUBMENU_DESIGN_CONFIGURATION_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-design-config"}
CONTENT_SUBMENU_DESIGN_THEMES_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-system-design-theme"}
CONTENT_SUBMENU_DESIGN_SCHEDULE_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-system-design-schedule"}
REPORTS_SUBMENU_PRODUCTS_IN_CART_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-shopcart-product"}
REPORTS_SUBMENU_SEARCH_TERMS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-search-term"}
REPORTS_SUBMENU_ABANDONED_CARTS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-shopcart-abandoned"}
REPORTS_SUBMENU_NEWSLETTER_PROBLEM_REPORTS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-newsletter-problem"}
REPORTS_SUBMENU_BY_CUSTOMERS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-review-customer"}
REPORTS_SUBMENU_BY_PRODUCTS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-review-product"}
REPORTS_SUBMENU_SALES_ORDERS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-salesroot-sales"}
REPORTS_SUBMENU_TAX_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-salesroot-tax"}
REPORTS_SUBMENU_INVOICED_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-salesroot-invoiced"}
REPORTS_SUBMENU_SHIPPING_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-salesroot-shipping"}
REPORTS_SUBMENU_REFUNDS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-report-salesroot-refunded"}
REPORTS_SUBMENU_COUPONS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-report-salesroot-coupons"}
REPORTS_SUBMENU_PAYPAL_SETTLEMENT_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-salesroot-paypal-settlement-reports"}
REPORTS_SUBMENU_BRAINTREE_SETTLEMENT_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-settlement-report"}
REPORTS_SUBMENU_ORDER_TOTAL_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-customers-totals"}
REPORTS_SUBMENU_ORDER_COUNT_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-customers-orders"}
REPORTS_SUBMENU_NEW_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-report-customers-accounts"}
REPORTS_SUBMENU_VIEWS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-report-products-viewed"}
REPORTS_SUBMENU_BESTSELLERS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-products-bestsellers"}
REPORTS_SUBMENU_LOW_STOCK_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-products-lowstock"}
REPORTS_SUBMENU_ORDERED_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-report-products-sold"}
REPORTS_SUBMENU_DOWNLOADS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-products-downloads"}
REPORTS_SUBMENU_REFRESH_STATISTICS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-products-sold"}
REPORTS_SUBMENU_ADVANCED_REPORTING_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-report-products-sold"}
REPORTS_SUBMENU_BI_ESSENTIALS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-bi-essentials"}
STORES_SUBMENU_ALL_STORES_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-system-store"}
STORES_SUBMENU_CONFIGURATION_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-system-config"}
STORES_SUBMENU_TERMS_AND_CONDITIONS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-sales-checkoutagreement"}
STORES_SUBMENU_ORDER_STATUS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-system-order-statuses"}
STORES_SUBMENU_SOURCES_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-source"}
STORES_SUBMENU_STOCKS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-stock"}
STORES_SUBMENU_TAX_RULES_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-sales-tax-rules"}
STORES_SUBMENU_TAX_ZONES_AND_RATES_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-sales-tax-rates"}
STORES_SUBMENU_CURRENCY_RATES_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-system-currency-rates"}
STORES_SUBMENU_CURRENCY_SYMBOLS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-system-currency-symbols"}
STORES_SUBMENU_PRODUCT_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-catalog-attributes-attributes"}
STORES_SUBMENU_ATTRIBUTE_SET_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-catalog-attributes-sets"}
STORES_SUBMENU_RATING_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-catalog-reviews-ratings-ratings"}
SYSTEM_SUBMENU_IMPORT_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-system-convert-import"}
SYSTEM_SUBMENU_EXPORT_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-system-convert-export"}
SYSTEM_SUBMENU_IMPORT_EXPORT_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-system-convert-tax"}
SYSTEM_SUBMENU_IMPORT_HISTORY_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-system-convert-history"}
SYSTEM_SUBMENU_INTEGRATIONS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-system-integrations"}
SYSTEM_SUBMENU_CACHE_MANAGEMENT_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-system-cache"}
SYSTEM_SUBMENU_INDEX_MANAGEMENT_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-system-index"}
SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-system-acl-users"}
SYSTEM_SUBMENU_LOCKED_USERS_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-system-acl-locks"}
SYSTEM_SUBMENU_USER_ROLES_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-system-acl-roles"}
SYSTEM_SUBMENU_BULK_ACTIONS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-system-magento-logging-bulk-operations"}
SYSTEM_SUBMENU_NOTIFICATIONS_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-system-adminnotification"}
SYSTEM_SUBMENU_CUSTOM_VARIABLES_LINK_LOCATOR: Dict[str, str] = {"strategy": "css", "locator": ".item-system-variable"}
SYSTEM_SUBMENU_MANAGE_ENCRYPTION_KEY_LINK_LOCATOR: Dict[str, str] = \
    {"strategy": "css", "locator": ".item-system-crypt-key"}
# Grids
GRID_FILTER_BUTTON_LOCATOR: Dict[str, str] = {"strategy": "xpath", "locator": "//button[text()=\"Filters\"]"}
