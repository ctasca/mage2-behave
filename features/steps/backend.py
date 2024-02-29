import time

from behave import *
from features.pages.backend.login import Login
from features.pages.backend.dashboard import Dashboard
from features.core_config.backend.backend_locators import (SALES_SUBMENU, CATALOG_SUBMENU, CUSTOMERS_SUBMENU,
                                                           MARKETING_SUBMENU, CONTENT_SUBMENU, REPORTS_SUBMENU,
                                                           STORES_SUBMENU, SYSTEM_SUBMENU)


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


@when(u'I want to view all my customers')
def step_impl(context):
    with Dashboard() as page:
        page.admin_menu.customers.click()
        page.admin_menu.submenu(CUSTOMERS_SUBMENU).all_customers.click()


@then(u'I should be viewing the customer grid')
def step_impl(context):
    assert 'customer/' in context.browser.url


@when(u'I am on the all customers grid')
def step_impl(context):
    view_all_customers_grid = 'When I want to view all my customers'
    context.execute_steps(f'''
        {view_all_customers_grid}
    ''')


@given("I am on the backend Dashboard page")
def step_impl(context):
    open_login_page = 'Given I am on the admin login page'
    fill_fields = 'When I enter my credentials'
    signin = 'And I sign in'
    context.execute_steps(f'''
            {open_login_page}
            {fill_fields}
            {signin}
        ''')


@then("I want to be able to reload data")
def step_impl(context):
    with Dashboard() as page:
        assert page.reload_data_button.is_visible(10)
        page.reload_data_button.click()


@when("I am on the sales orders grid")
def step_impl(context):
    with Dashboard() as page:
        page.admin_menu.sales.click()
        page.admin_menu.submenu(SALES_SUBMENU).orders.click()
