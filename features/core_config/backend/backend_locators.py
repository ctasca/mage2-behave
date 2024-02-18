# Login form
ADMIN_LOGIN_FORM_USERNAME_LOCATOR = {'strategy':'id', 'locator':'username'}
ADMIN_LOGIN_FORM_PASSWORD_LOCATOR = {'strategy':'id', 'locator':'login'}
ADMIN_LOGIN_FORM_SIGNIN_BUTTON_LOCATOR = {'strategy':'css', 'locator':'.action-login.action-primary'}
# Admin menu
ADMIN_MENU_ROOT = {'strategy':'css', 'locator':'.admin__menu'}
ADMIN_MENU_DASHBOARD_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-dashboard'}
ADMIN_MENU_SALES_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-sales'}
ADMIN_MENU_CATALOG_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-catalog'}
ADMIN_MENU_CUSTOMERS_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-customer'}
ADMIN_MENU_MARKETING_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-marketing'}
ADMIN_MENU_CONTENT_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-content'}
ADMIN_MENU_REPORTS_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-reports'}
ADMIN_MENU_STORES_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-stores'}
ADMIN_MENU_SYSTEM_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-system'}
# Admin menu submenus
SALES_SUBMENU_ORDERS_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-sales-order'}
SALES_SUBMENU_INVOICES_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-sales-order'}
SALES_SUBMENU_SHIPMENTS_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-sales-shipment'}
SALES_SUBMENU_CREDITMEMOS_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-sales-creditmemo'}
SALES_SUBMENU_BILLING_AGREEMENTS_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-paypal-billing-agreement'}
SALES_SUBMENU_TRANSACTIONS_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-sales-transactions'}
SALES_SUBMENU_VIRTUAL_TERMINAL_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-virtual-terminal'}
CATALOG_SUBMENU_PRODUCTS_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-catalog-products'}
CATALOG_SUBMENU_CATEGORIES_LINK_LOCATOR = {'strategy':'css', 'locator':'.item-catalog-categories'}
CUSTOMERS_SUBMENU_ALL_CUSTOMERS_LINK_LOCATOR =  {'strategy':'css','locator':'.item-customer-manage'}
CUSTOMERS_SUBMENU_ONLINE_LINK_LOCATOR =  {'strategy':'css','locator':'.item-customer-online'}
CUSTOMERS_SUBMENU_AS_CUSTOMER_LOG_LINK_LOCATOR =  {'strategy':'css','locator':'.item-login-log'}
CUSTOMERS_SUBMENU_GROUPS_LINK_LOCATOR =  {'strategy':'css','locator':'.item-customer-group'}
MARKETING_SUBMENU_CATALOG_PRICE_RULE_LINK_LOCATOR = {'strategy':'css','locator':'.item-promo-catalog'}
MARKETING_SUBMENU_CART_PRICE_RULES_LINK_LOCATOR = {'strategy':'css','locator':'.item-promo-quote'}
MARKETING_SUBMENU_EMAIL_TEMPLATES_LINK_LOCATOR = {'strategy':'css','locator':'.item-template'}
MARKETING_SUBMENU_NEWSLETTER_TEMPLATES_LINK_LOCATOR = {'strategy':'css','locator':'.item-newsletter-template'}
MARKETING_SUBMENU_NEWSLETTER_QUEUE_LINK_LOCATOR = {'strategy':'css','locator':'.item-newsletter-queue'}
MARKETING_SUBMENU_NEWSLETTER_SUBSCIBERS_LINK_LOCATOR = {'strategy':'css','locator':'.item-newsletter-subscriber'}
MARKETING_SUBMENU_URL_REWRITES_LINK_LOCATOR = {'strategy':'css','locator':'.item-urlrewrite'}
MARKETING_SUBMENU_SEARCH_TERMS_LINK_LOCATOR = {'strategy':'css','locator':'.item-search-terms'}
MARKETING_SUBMENU_SEARCH_SYNONYMS_LINK_LOCATOR = {'strategy':'css','locator':'.item-search-synonyms'}
MARKETING_SUBMENU_SITE_MAP_LINK_LOCATOR = {'strategy':'css','locator':'.item-catalog-sitemap'}
MARKETING_SUBMENU_ALL_REVIEWS_LINK_LOCATOR = {'strategy':'css','locator':'.item-catalog-reviews-ratings-reviews-all'}
MARKETING_SUBMENU_PENDING_REVIEWS_LINK_LOCATOR = {'strategy':'css','locator':'.item-catalog-reviews-ratings-pending'}
# Using xpath strategy for Pages link as had test is_visible failure via css strategy
CONTENT_SUBMENU_PAGES_LINK_LOCATOR = {'strategy':'xpath','locator':"//a[.//span[text()='Pages']]"}
CONTENT_SUBMENU_BLOCKS_LINK_LOCATOR = {'strategy':'css','locator':'.item-cms-block'}
CONTENT_SUBMENU_WIDGETS_LINK_LOCATOR = {'strategy':'css','locator':'.item-cms-widget-instance'}
CONTENT_SUBMENU_TEMPLATES_LINK_LOCATOR = {'strategy':'css','locator':'.item-templates'}
CONTENT_SUBMENU_MEDIA_GALLERY_LINK_LOCATOR = {'strategy':'css','locator':'.item-media-gallery'}
CONTENT_SUBMENU_DESIGN_CONFIGURATION_LINK_LOCATOR = {'strategy':'css','locator':'.item-design-config'}
CONTENT_SUBMENU_DESIGN_THEMES_LINK_LOCATOR = {'strategy':'css','locator':'.item-system-design-theme'}
CONTENT_SUBMENU_DESIGN_SCHEDULE_LINK_LOCATOR = {'strategy':'css','locator':'.item-system-design-schedule'}
# Grids
GRID_FILTER_BUTTON_LOCATOR = {'strategy':'xpath', 'locator':"//button[text()='Filters']"}

