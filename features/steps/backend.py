import time

from behave import *
from features.pages.backend.login import Login
from features.pages.backend.dashboard import Dashboard
from features.pages.backend.customers_grid import CustomersGrid


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
        page.admin_menu.submenus['customers'].all_customers.click()


@then(u'I should be viewing the customer grid')
def step_impl(context):
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
        filters = page.customers_grid_filters
        filters.get_filter(filters.FROM_ID_FILTER).fill(10)
        filters.get_filter(filters.TO_ID_FILTER).fill(20)
        filters.get_filter(filters.EMAIL_FILTER).fill('test@test.com')
        filters.get_filter(filters.NAME_FILTER).fill('Test')
        created_at_from_datepicker = filters.get_filter(filters.CREATED_AT_FROM_DATAPICKER)
        created_at_from_datepicker.click()
        created_at_from_datepicker.select_month('May')
        created_at_from_datepicker.select_year('2000')
        created_at_from_datepicker.click_day('31')
        created_at_to_datepicker = filters.get_filter(filters.CREATED_AT_TO_DATAPICKER)
        created_at_to_datepicker.click()
        created_at_to_datepicker.select_month('Jun')
        created_at_to_datepicker.select_year('2022')
        created_at_to_datepicker.click_day('15')
        dob_from_datepicker = filters.get_filter(filters.DOB_FROM_DATAPICKER)
        dob_from_datepicker.click()
        dob_from_datepicker.select_month('Apr')
        dob_from_datepicker.select_year('1985')
        dob_from_datepicker.click_day('5')
        dob_to_datepicker = filters.get_filter(filters.DOB_TO_DATAPICKER)
        dob_to_datepicker.click()
        dob_to_datepicker.hide()
        filters.get_filter(filters.GENDER_FILTER).select('Male', 10)
        filters.get_filter(filters.WEBSITE_ID_FILTER).select('Main Website', 10)
        page.apply_filters_button.click()
        assert page.browser.is_text_present("We couldn't find any records.") is True


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
