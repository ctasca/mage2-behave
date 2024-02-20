from behave import *
from pages.backend.login import Login
from pages.backend.dashboard import Dashboard
from pages.backend.customers_grid import CustomersGrid
import time

@given(u'I am on the admin login page')
def step_impl(context):
    with Login() as page:
        page.base_url = context.baseurl
        page.url_suffix = context.backend + 'login'
        page.navigate()

@when(u'I enter my credentials')
def step_impl(context):
    with Login() as page:
        page.form.username.fill(context.admin_username)
        page.form.password.fill(context.admin_password)

@when(u'I sign in')
def step_impl(context):
    with Login() as page:
        page.form.signin.click()

@then(u'I should see a dashboard header')
def step_impl(context):
    assert context.browser.is_text_present("Dashboard") is True

@given(u'I am logged in the backend')
def step_impl(context):
    open_login_page = 'Given I am on the admin login page'
    fill_fields = 'When I enter my credentials'
    signin = 'And I sign in'
    context.execute_steps(f'''
        {open_login_page}
        {fill_fields}
        {signin}
    ''')

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
        
        

@when(u'I want to view all my customers')
def step_impl(context):
    with Dashboard() as page:
        page.admin_menu.customers.click()
        page.admin_menu.submenus['customers'].all_customers.click()


@then(u'I should be viewing the customer grid')
def step_impl(context):
    with CustomersGrid() as page:
        assert 'customer/' in context.browser.url 

@when(u'I am on the all customers grid')
def step_impl(context):
    view_all_customers_grid = 'When I want to view all my customers'
    context.execute_steps(f'''
        {view_all_customers_grid}
    ''')

@then(u'I want to be able to apply filters for searching purposes')
def step_impl(context):
    with CustomersGrid() as page:
        page.filters_button.click()



