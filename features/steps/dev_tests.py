from behave import *
from features.pages.backend.dashboard import Dashboard
from features.pages.backend.customers_grid import CustomersGrid
from features.pages.backend.utils.ui_grid import reset_all_active_filters


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
            sales_submenu_links = page.admin_menu.submenu('sales').links()
            assert all(link.is_visible(10) for link in sales_submenu_links)

        if item == 'Catalog':
            catalog_submenu_links = page.admin_menu.submenu('catalog').links()
            assert all(link.is_visible(10) for link in catalog_submenu_links)

        if item == 'Customers':
            customer_submenu_links = page.admin_menu.submenu('customers').links()
            assert all(link.is_visible(10) for link in customer_submenu_links)

        if item == 'Marketing':
            marketing_submenus_links = page.admin_menu.submenu('marketing').links()
            assert all(link.is_visible(10) for link in marketing_submenus_links)

        if item == 'Content':
            content_submenus_links = page.admin_menu.submenu('content').links()
            assert all(link.is_visible(10) for link in content_submenus_links)

        if item == 'Reports':
            report_submenus_links = page.admin_menu.submenu('reports').links()
            assert all(link.is_visible(10) for link in report_submenus_links)

        if item == 'Stores':
            stores_submenus_links = page.admin_menu.submenu('stores').links()
            assert all(link.is_visible(10) for link in stores_submenus_links)

        if item == 'System':
            system_submenus_links = page.admin_menu.submenu('system').links()
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
        page.fulltext_search_input.fill('search text')
        page.filters_button.click()
        page.fulltext_search_button.click()
        assert page.browser.is_text_present("We couldn't find any records.") is True


@step("I want to be able to reset the applied filters")
def step_impl(context):
    with CustomersGrid() as page:
        active_filters = page.active_filters_buttons.children()
        reset_all_active_filters(active_filters)
