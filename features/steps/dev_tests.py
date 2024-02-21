from behave import *
from features.pages.backend.dashboard import Dashboard


@when(u'I click the "{item}" menu item')
def step_impl(context, item):
    with Dashboard() as page:
        if item == 'Sales':
            page.admin_menu.sales.click()
        if item == 'Catalog':
            page.admin_menu.catalog.click()
        if item == 'Customers':
            page.admin_menu.customers.click()
        if item == 'Marketing':
            page.admin_menu.marketing.click()
        if item == 'Content':
            page.admin_menu.content.click()
        if item == 'Reports':
            page.admin_menu.reports.click()
        if item == 'Stores':
            page.admin_menu.stores.click()
        if item == 'System':
            page.admin_menu.system.click()


@then(u'I should see the "{item}" submenu links')
def step_impl(context, item):
    with Dashboard() as page:
        if item == "Sales":
            assert page.admin_menu.submenus['sales'].orders.is_visible() is True
            assert page.admin_menu.submenus['sales'].invoices.is_visible() is True
            assert page.admin_menu.submenus['sales'].shipments.is_visible() is True
            assert page.admin_menu.submenus['sales'].creditmemos.is_visible() is True
            assert page.admin_menu.submenus['sales'].billing_agreements.is_visible() is True
            assert page.admin_menu.submenus['sales'].transactions.is_visible() is True
            assert page.admin_menu.submenus['sales'].virtual_terminal.is_visible() is True

        if item == 'Catalog':
            assert page.admin_menu.submenus['catalog'].products.is_visible() is True
            assert page.admin_menu.submenus['catalog'].categories.is_visible() is True

        if item == 'Customers':
            assert page.admin_menu.submenus['customers'].all_customers.is_visible() is True
            assert page.admin_menu.submenus['customers'].now_online.is_visible() is True
            assert page.admin_menu.submenus['customers'].login_as_customer_log.is_visible() is True
            assert page.admin_menu.submenus['customers'].customer_groups.is_visible() is True

        if item == 'Marketing':
            assert page.admin_menu.submenus['marketing'].catalog_price_rule.is_visible() is True
            assert page.admin_menu.submenus['marketing'].cart_price_rules.is_visible() is True
            assert page.admin_menu.submenus['marketing'].email_templates.is_visible() is True
            assert page.admin_menu.submenus['marketing'].newsletter_templates.is_visible() is True
            assert page.admin_menu.submenus['marketing'].newsletter_queue.is_visible() is True
            assert page.admin_menu.submenus['marketing'].newsletter_subscribers.is_visible() is True
            assert page.admin_menu.submenus['marketing'].url_rewrites.is_visible() is True
            assert page.admin_menu.submenus['marketing'].search_terms.is_visible() is True
            assert page.admin_menu.submenus['marketing'].search_synonyms.is_visible() is True
            assert page.admin_menu.submenus['marketing'].site_map.is_visible() is True
            assert page.admin_menu.submenus['marketing'].all_reviews.is_visible() is True
            assert page.admin_menu.submenus['marketing'].pending_reviews.is_visible() is True

        if item == 'Content':
            assert page.admin_menu.submenus['content'].pages.is_visible() is True
            assert page.admin_menu.submenus['content'].blocks.is_visible() is True
            assert page.admin_menu.submenus['content'].widgets.is_visible() is True
            assert page.admin_menu.submenus['content'].templates.is_visible() is True
            assert page.admin_menu.submenus['content'].media_gallery.is_visible() is True
            assert page.admin_menu.submenus['content'].design_configuration.is_visible() is True
            assert page.admin_menu.submenus['content'].design_themes.is_visible() is True
            assert page.admin_menu.submenus['content'].design_schedule.is_visible() is True

        if item == 'Reports':
            assert page.admin_menu.submenus['reports'].products_in_cart.is_visible() is True
            assert page.admin_menu.submenus['reports'].search_terms.is_visible() is True
            assert page.admin_menu.submenus['reports'].abandoned_carts.is_visible() is True
            assert page.admin_menu.submenus['reports'].newsletter_problem_reports.is_visible() is True
            assert page.admin_menu.submenus['reports'].by_customers.is_visible() is True
            assert page.admin_menu.submenus['reports'].by_products.is_visible() is True
            assert page.admin_menu.submenus['reports'].orders.is_visible() is True
            assert page.admin_menu.submenus['reports'].tax.is_visible() is True
            assert page.admin_menu.submenus['reports'].invoiced.is_visible() is True
            assert page.admin_menu.submenus['reports'].shipping.is_visible() is True
            assert page.admin_menu.submenus['reports'].refunds.is_visible() is True
            assert page.admin_menu.submenus['reports'].coupons.is_visible() is True
            assert page.admin_menu.submenus['reports'].paypal_settlement.is_visible() is True
            assert page.admin_menu.submenus['reports'].braintree_settlement.is_visible() is True
            assert page.admin_menu.submenus['reports'].order_total.is_visible() is True
            assert page.admin_menu.submenus['reports'].order_count.is_visible() is True
            assert page.admin_menu.submenus['reports'].new.is_visible() is True
            assert page.admin_menu.submenus['reports'].views.is_visible() is True
            assert page.admin_menu.submenus['reports'].bestsellers.is_visible() is True
            assert page.admin_menu.submenus['reports'].low_stock.is_visible() is True
            assert page.admin_menu.submenus['reports'].ordered.is_visible() is True
            assert page.admin_menu.submenus['reports'].downloads.is_visible() is True
            assert page.admin_menu.submenus['reports'].refresh_statistics.is_visible() is True
            assert page.admin_menu.submenus['reports'].advanced_reporting.is_visible() is True
            assert page.admin_menu.submenus['reports'].bi_essentials.is_visible() is True

        if item == 'Stores':
            assert page.admin_menu.submenus['stores'].all_stores.is_visible() is True
            assert page.admin_menu.submenus['stores'].configuration.is_visible() is True
            assert page.admin_menu.submenus['stores'].terms_and_conditions.is_visible() is True
            assert page.admin_menu.submenus['stores'].order_status.is_visible() is True
            assert page.admin_menu.submenus['stores'].sources.is_visible() is True
            assert page.admin_menu.submenus['stores'].stocks.is_visible() is True
            assert page.admin_menu.submenus['stores'].tax_rules.is_visible() is True
            assert page.admin_menu.submenus['stores'].tax_zones_and_rates.is_visible() is True
            assert page.admin_menu.submenus['stores'].currency_rates.is_visible() is True
            assert page.admin_menu.submenus['stores'].currency_symbols.is_visible() is True
            assert page.admin_menu.submenus['stores'].product.is_visible() is True
            assert page.admin_menu.submenus['stores'].attribute_set.is_visible() is True
            assert page.admin_menu.submenus['stores'].rating.is_visible() is True

        if item == 'System':
            assert page.admin_menu.submenus['system'].system_import.is_visible() is True
            assert page.admin_menu.submenus['system'].export.is_visible() is True
            assert page.admin_menu.submenus['system'].import_export_tax_rates.is_visible() is True
            assert page.admin_menu.submenus['system'].import_history.is_visible() is True
            assert page.admin_menu.submenus['system'].integrations.is_visible() is True
            assert page.admin_menu.submenus['system'].cache_management.is_visible() is True
            assert page.admin_menu.submenus['system'].index_management.is_visible() is True
            assert page.admin_menu.submenus['system'].all_users.is_visible() is True
            assert page.admin_menu.submenus['system'].locked_users.is_visible() is True
            assert page.admin_menu.submenus['system'].user_roles.is_visible() is True
            assert page.admin_menu.submenus['system'].bulk_actions.is_visible() is True
            assert page.admin_menu.submenus['system'].notifications.is_visible() is True
            assert page.admin_menu.submenus['system'].custom_variables.is_visible() is True
            assert page.admin_menu.submenus['system'].manage_encryption_key.is_visible() is True

