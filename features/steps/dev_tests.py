from behave import *
from features.pages.backend.dashboard import Dashboard
from features.pages.backend.customers_grid import CustomersGrid
from features.pages.backend.sales_orders_grid import SalesOrdersGrid
from features.core_config.backend.backend_locators import (SALES_SUBMENU, CATALOG_SUBMENU, CUSTOMERS_SUBMENU,
                                                           MARKETING_SUBMENU, CONTENT_SUBMENU, REPORTS_SUBMENU,
                                                           STORES_SUBMENU, SYSTEM_SUBMENU)


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
            sales_submenu_links = page.admin_menu.submenu(SALES_SUBMENU).links()
            assert all(link.is_visible(10) for link in sales_submenu_links)

        if item == 'Catalog':
            catalog_submenu_links = page.admin_menu.submenu(CATALOG_SUBMENU).links()
            assert all(link.is_visible(10) for link in catalog_submenu_links)

        if item == 'Customers':
            customer_submenu_links = page.admin_menu.submenu(CUSTOMERS_SUBMENU).links()
            assert all(link.is_visible(10) for link in customer_submenu_links)

        if item == 'Marketing':
            marketing_submenus_links = page.admin_menu.submenu(MARKETING_SUBMENU).links()
            assert all(link.is_visible(10) for link in marketing_submenus_links)

        if item == 'Content':
            content_submenus_links = page.admin_menu.submenu(CONTENT_SUBMENU).links()
            assert all(link.is_visible(10) for link in content_submenus_links)

        if item == 'Reports':
            report_submenus_links = page.admin_menu.submenu(REPORTS_SUBMENU).links()
            assert all(link.is_visible(10) for link in report_submenus_links)

        if item == 'Stores':
            stores_submenus_links = page.admin_menu.submenu(STORES_SUBMENU).links()
            assert all(link.is_visible(10) for link in stores_submenus_links)

        if item == 'System':
            system_submenus_links = page.admin_menu.submenu(SYSTEM_SUBMENU).links()
            assert all(link.is_visible(10) for link in system_submenus_links)


@when("I want to change store scope")
def step_impl(context):
    assert True is not False


@then("I should be able to select the store I want to switch to")
def step_impl(context):
    with Dashboard() as page:
        page.store_switcher.switch_to_store('Default Store View')


@then("I want to be able to choose and view the diagram tabs")
def step_impl(context):
    with Dashboard() as page:
        assert page.dashboard_diagram.orders_tab.is_visible(10) is True
        assert page.dashboard_diagram.amounts_tab.is_visible(10) is True
        page.dashboard_diagram.orders_tab.click()
        page.dashboard_diagram.amounts_tab.click()


@then("I want to be able to choose and view the store statistics tabs")
def step_impl(context):
    with Dashboard() as page:
        assert page.dashboard_store_stats.bestsellers_tab.is_visible(10) is True
        assert page.dashboard_store_stats.most_viewed_products_tab.is_visible(10) is True
        assert page.dashboard_store_stats.new_customers_tab.is_visible(10) is True
        assert page.dashboard_store_stats.customers_tab.is_visible(10) is True
        page.dashboard_store_stats.bestsellers_tab.click()
        page.dashboard_store_stats.most_viewed_products_tab.click()
        page.dashboard_store_stats.new_customers_tab.click()
        page.dashboard_store_stats.customers_tab.click()


@given("I want to create a dummy customer for my tests")
def step_impl(context):
    pass


@when("the request is made")
def step_impl(context):
    pass


@then("I should have a context dummy customer id")
def step_impl(context):
    assert context.dummy_customer_id is not None


@given("I have needed products in stock")
def step_impl(context):
    pass


@then("I should be able to add them to my shopping cart")
def step_impl(context):
    pass


@given("I have products out of in stock")
def step_impl(context):
    pass


@then("I should not be able to add them to my shopping cart")
def step_impl(context):
    pass


@then("I want to be able to use the search fulltext input to filter the grid")
def step_impl(context):
    with CustomersGrid() as page:
        filters = page.customers_grid_filters
        filters.fulltext_search('text')
        assert page.browser.is_text_present("We couldn't find any records.") is True


@then("I want to be able to reset the applied filters")
def step_impl(context):
    with CustomersGrid() as page:
        filters = page.customers_grid_filters
        filters.clear_all()
        assert filters.get_root().is_not_visible(10) is True


@then(u'I want to be able to apply filters to customers for searching purposes')
def step_impl(context):
    with CustomersGrid() as page:
        filters = page.customers_grid_filters
        filters.start_filtering()
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
        created_at_to_datepicker.go_to_today()
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
        filters.apply_filters()


@then("I want to be able to apply filters to orders for searching purposes")
def step_impl(context):
    with SalesOrdersGrid() as page:
        filters = page.orders_grid_filters
        filters.start_filtering()
        created_at_from_datepicker = filters.get_filter(filters.CREATED_AT_FROM_DATAPICKER)
        created_at_from_datepicker.click()
        created_at_from_datepicker.select_month('May')
        created_at_from_datepicker.select_year('2000')
        created_at_from_datepicker.click_day('31')
        created_at_to_datepicker = filters.get_filter(filters.CREATED_AT_TO_DATAPICKER)
        created_at_to_datepicker.click()
        created_at_to_datepicker.go_to_today()
        base_grand_total_from = filters.get_filter(filters.BASE_GRAND_TOTAL_FROM)
        base_grand_total_from.fill(100)
        base_grand_total_to = filters.get_filter(filters.BASE_GRAND_TOTAL_TO)
        base_grand_total_to.fill(200)
        purchased_grand_total_from = filters.get_filter(filters.PURCHASED_GRAND_TOTAL_FROM)
        purchased_grand_total_from.fill(300)
        purchased_grand_total_to = filters.get_filter(filters.PURCHASED_GRAND_TOTAL_TO)
        purchased_grand_total_to.fill(400)
        filters.apply_filters()
