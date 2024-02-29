from typing import Dict
from ..locators import STRATEGY_KEY, LOCATOR_KEY, XPATH_STRATEGY, ID_STRATEGY, CSS_STRATEGY

ADMIN_LOGIN_FORM_USERNAME_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "username"}
ADMIN_LOGIN_FORM_PASSWORD_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "login"}
ADMIN_LOGIN_FORM_SIGNIN_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".action-login.action-primary"}
# Admin menu
ADMIN_MENU_ROOT: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "nav"}
ADMIN_MENU_DASHBOARD_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-backend-dashboard"}
ADMIN_MENU_SALES_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-sales-sales"}
ADMIN_MENU_CATALOG_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-catalog-catalog"}
ADMIN_MENU_CUSTOMERS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-customer-customer"}
ADMIN_MENU_MARKETING_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-backend-marketing"}
ADMIN_MENU_CONTENT_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-backend-content"}
ADMIN_MENU_REPORTS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-reports-report"}
ADMIN_MENU_STORES_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-backend-stores"}
ADMIN_MENU_SYSTEM_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "menu-magento-backend-system"}
# Admin menu submenus
SALES_SUBMENU: str = 'sales'
SALES_SUBMENU_ORDERS_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-sales-order"}
SALES_SUBMENU_INVOICES_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-sales-order"}
SALES_SUBMENU_SHIPMENTS_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-sales-shipment"}
SALES_SUBMENU_CREDITMEMOS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-sales-creditmemo"}
SALES_SUBMENU_BILLING_AGREEMENTS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-paypal-billing-agreement"}
SALES_SUBMENU_TRANSACTIONS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-sales-transactions"}
SALES_SUBMENU_VIRTUAL_TERMINAL_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-virtual-terminal"}
CATALOG_SUBMENU: str = 'catalog'
CATALOG_SUBMENU_PRODUCTS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-catalog-products"}
CATALOG_SUBMENU_CATEGORIES_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-catalog-categories"}
CUSTOMERS_SUBMENU: str = 'customers'
CUSTOMERS_SUBMENU_ALL_CUSTOMERS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-customer-manage"}
CUSTOMERS_SUBMENU_ONLINE_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-customer-online"}
CUSTOMERS_SUBMENU_AS_CUSTOMER_LOG_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-login-log"}
CUSTOMERS_SUBMENU_GROUPS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-customer-group"}
MARKETING_SUBMENU: str = 'marketing'
MARKETING_SUBMENU_CATALOG_PRICE_RULE_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-promo-catalog"}
MARKETING_SUBMENU_CART_PRICE_RULES_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-promo-quote"}
MARKETING_SUBMENU_EMAIL_TEMPLATES_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-template"}
MARKETING_SUBMENU_NEWSLETTER_TEMPLATES_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-newsletter-template"}
MARKETING_SUBMENU_NEWSLETTER_QUEUE_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-newsletter-queue"}
MARKETING_SUBMENU_NEWSLETTER_SUBSCIBERS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-newsletter-subscriber"}
MARKETING_SUBMENU_URL_REWRITES_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-urlrewrite"}
MARKETING_SUBMENU_SEARCH_TERMS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-search-terms"}
MARKETING_SUBMENU_SEARCH_SYNONYMS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-search-synonyms"}
MARKETING_SUBMENU_SITE_MAP_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-catalog-sitemap"}
MARKETING_SUBMENU_ALL_REVIEWS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-catalog-reviews-ratings-reviews-all"}
MARKETING_SUBMENU_PENDING_REVIEWS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-catalog-reviews-ratings-pending"}
CONTENT_SUBMENU: str = 'content'
CONTENT_SUBMENU_PAGES_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-cms-page"}
CONTENT_SUBMENU_BLOCKS_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-cms-block"}
CONTENT_SUBMENU_WIDGETS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-cms-widget-instance"}
CONTENT_SUBMENU_TEMPLATES_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-templates"}
CONTENT_SUBMENU_MEDIA_GALLERY_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-media-gallery"}
CONTENT_SUBMENU_DESIGN_CONFIGURATION_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-design-config"}
CONTENT_SUBMENU_DESIGN_THEMES_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-design-theme"}
CONTENT_SUBMENU_DESIGN_SCHEDULE_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-design-schedule"}
REPORTS_SUBMENU: str = 'reports'
REPORTS_SUBMENU_PRODUCTS_IN_CART_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-shopcart-product"}
REPORTS_SUBMENU_SEARCH_TERMS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-search-term"}
REPORTS_SUBMENU_ABANDONED_CARTS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-shopcart-abandoned"}
REPORTS_SUBMENU_NEWSLETTER_PROBLEM_REPORTS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-newsletter-problem"}
REPORTS_SUBMENU_BY_CUSTOMERS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-review-customer"}
REPORTS_SUBMENU_BY_PRODUCTS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-review-product"}
REPORTS_SUBMENU_SALES_ORDERS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-salesroot-sales"}
REPORTS_SUBMENU_TAX_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-salesroot-tax"}
REPORTS_SUBMENU_INVOICED_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-salesroot-invoiced"}
REPORTS_SUBMENU_SHIPPING_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-salesroot-shipping"}
REPORTS_SUBMENU_REFUNDS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-salesroot-refunded"}
REPORTS_SUBMENU_COUPONS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-salesroot-coupons"}
REPORTS_SUBMENU_PAYPAL_SETTLEMENT_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-salesroot-paypal-settlement-reports"}
REPORTS_SUBMENU_BRAINTREE_SETTLEMENT_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-settlement-report"}
REPORTS_SUBMENU_ORDER_TOTAL_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-customers-totals"}
REPORTS_SUBMENU_ORDER_COUNT_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-customers-orders"}
REPORTS_SUBMENU_NEW_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-customers-accounts"}
REPORTS_SUBMENU_VIEWS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-products-viewed"}
REPORTS_SUBMENU_BESTSELLERS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-products-bestsellers"}
REPORTS_SUBMENU_LOW_STOCK_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-products-lowstock"}
REPORTS_SUBMENU_ORDERED_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-products-sold"}
REPORTS_SUBMENU_DOWNLOADS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-products-downloads"}
REPORTS_SUBMENU_REFRESH_STATISTICS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-products-sold"}
REPORTS_SUBMENU_ADVANCED_REPORTING_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-report-products-sold"}
REPORTS_SUBMENU_BI_ESSENTIALS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-bi-essentials"}
STORES_SUBMENU: str = 'stores'
STORES_SUBMENU_ALL_STORES_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-store"}
STORES_SUBMENU_CONFIGURATION_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-config"}
STORES_SUBMENU_TERMS_AND_CONDITIONS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-sales-checkoutagreement"}
STORES_SUBMENU_ORDER_STATUS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-order-statuses"}
STORES_SUBMENU_SOURCES_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-source"}
STORES_SUBMENU_STOCKS_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-stock"}
STORES_SUBMENU_TAX_RULES_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-sales-tax-rules"}
STORES_SUBMENU_TAX_ZONES_AND_RATES_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-sales-tax-rates"}
STORES_SUBMENU_CURRENCY_RATES_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-currency-rates"}
STORES_SUBMENU_CURRENCY_SYMBOLS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-currency-symbols"}
STORES_SUBMENU_PRODUCT_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-catalog-attributes-attributes"}
STORES_SUBMENU_ATTRIBUTE_SET_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-catalog-attributes-sets"}
STORES_SUBMENU_RATING_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-catalog-reviews-ratings-ratings"}
SYSTEM_SUBMENU: str = 'system'
SYSTEM_SUBMENU_IMPORT_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-convert-import"}
SYSTEM_SUBMENU_EXPORT_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-convert-export"}
SYSTEM_SUBMENU_IMPORT_EXPORT_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-convert-tax"}
SYSTEM_SUBMENU_IMPORT_HISTORY_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-convert-history"}
SYSTEM_SUBMENU_INTEGRATIONS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-integrations"}
SYSTEM_SUBMENU_CACHE_MANAGEMENT_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-cache"}
SYSTEM_SUBMENU_INDEX_MANAGEMENT_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-index"}
SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-acl-users"}
SYSTEM_SUBMENU_LOCKED_USERS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-acl-locks"}
SYSTEM_SUBMENU_USER_ROLES_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-acl-roles"}
SYSTEM_SUBMENU_BULK_ACTIONS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-magento-logging-bulk-operations"}
SYSTEM_SUBMENU_NOTIFICATIONS_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-adminnotification"}
SYSTEM_SUBMENU_CUSTOM_VARIABLES_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-variable"}
SYSTEM_SUBMENU_MANAGE_ENCRYPTION_KEY_LINK_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: CSS_STRATEGY, LOCATOR_KEY: ".item-system-crypt-key"}
# Store Scopes
STORE_CHANGE_BUTTON_LINK_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "store-change-button"}
STORE_SCOPE_LIST_ROOT_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//ul[@data-role='stores-list']"}
SET_STORE_SCOPE_LOCATOR_FORMAT: str = "//a[contains(text(), '{}')]"
# Grids
GRID_FILTER_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "(//div[@class=\"data-grid-filters-action-wrap\"]//button["
                                                "@data-action=\"grid-filter-expand\"])[1]"}
GRID_FULLTEXT_INPUT_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "fulltext"}
GRID_FULLTEXT_SEARCH_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "(//div[@class='data-grid-search-control-wrap']/button)[1]"}
GRID_ACTIVE_FILTERS_ROOT_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: '(//ul[@data-role="filter-list"]//li)[1]'}
GRID_ACTIVE_FILERS_BUTTON_LOCATOR: Dict[str, str] = {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: './button'}
GRID_APPLY_FILTERS_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//button[@data-action='grid-filter-apply']"}
GRID_FILTERS_ROOT_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: '//div[@data-part="filter-form"]'}
# Dashboard page
DASHBOARD_RELOAD_DATA_BUTTON_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//button[@title=\"Reload Data\"]"}
DASHBOARD_DIAGRAM_ORDER_TAB_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "diagram_tab_orders"}
DASHBOARD_DIAGRAM_AMOUNTS_TAB_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "diagram_tab_amounts"}
DASHBOARD_BESTSELLERS_TAB_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "grid_tab_ordered_products"}
DASHBOARD_REVIEWED_PRODUCTS_TAB_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "grid_tab_reviewed_products"}
DASHBOARD_NEW_CUSTOMERS_TAB_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "grid_tab_new_customers"}
DASHBOARD_CUSTOMERS_TAB_LOCATOR: Dict[str, str] = {STRATEGY_KEY: ID_STRATEGY, LOCATOR_KEY: "grid_tab_customers"}
# Customers grid filters
CUSTOMERS_FROM_ID_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"entity_id[from]\"]"}
CUSTOMERS_TO_ID_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"entity_id[to]\"]"}
CUSTOMERS_CREATED_FROM_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"created_at[from]\"]"}
CUSTOMERS_CREATED_TO_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"created_at[to]\"]"}
CUSTOMERS_DOB_FROM_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"dob[from]\"]"}
CUSTOMERS_DOB_TO_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"dob[to]\"]"}
CUSTOMERS_EMAIL_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"email\"]"}
CUSTOMERS_NAME_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"name\"]"}
CUSTOMERS_TAX_VAT_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"taxvat\"]"}
CUSTOMERS_TELEPHONE_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"billing_telephone\"]"}
CUSTOMERS_POSTCODE_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"billing_postcode\"]"}
CUSTOMERS_REGION_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"billing_region\"]"}
CUSTOMERS_GROUP_SELECT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//select[@name=\"group_id\"]"}
CUSTOMERS_COUNTRY_SELECT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//select[@name=\"billing_country_id\"]"}
CUSTOMERS_WEBSITE_SELECT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//select[@name=\"website_id\"]"}
CUSTOMERS_GENDER_SELECT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//select[@name=\"website_id\"]"}
