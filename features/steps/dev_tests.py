import mariadb
from behave import *
from features.core_config.backend.locators.admin_submenus import *
from features.pages.backend.dashboard import Dashboard
from features.pages.backend.customers_grid import CustomersGrid
from features.pages.backend.sales_orders_grid import SalesOrdersGrid


@when(u'I click the "{item}" menu item')
def step_impl(context, item):
    with Dashboard() as page:
        if item == 'Sales':
            page.admin_menu.get_link('sales').click()
        if item == 'Catalog':
            page.admin_menu.get_link('catalog').click()
        if item == 'Customers':
            page.admin_menu.get_link('customers').click()
        if item == 'Marketing':
            page.admin_menu.get_link('marketing').click()
        if item == 'Content':
            page.admin_menu.get_link('content').click()
        if item == 'Reports':
            page.admin_menu.get_link('reports').click()
        if item == 'Stores':
            page.admin_menu.get_link('stores').click()
        if item == 'System':
            page.admin_menu.get_link('system').click()


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
        filters = page.grid_filters
        filters.fulltext_search('text')
        assert page.browser.is_text_present("We couldn't find any records.") is True


@then("I want to be able to reset the customers grid applied filters")
def step_impl(context):
    with CustomersGrid() as page:
        filters = page.grid_filters
        filters.clear_all(1)
        assert filters.get_root().is_not_visible(10) is True


@then("I want to be able to reset the sales orders grid applied filters")
def step_impl(context):
    with SalesOrdersGrid() as page:
        filters = page.grid_filters
        filters.clear_all(1)
        assert filters.get_root().is_not_visible(10) is True


@then(u'I want to be able to apply filters to customers for searching purposes')
def step_impl(context):
    with CustomersGrid() as page:
        filters = page.grid_filters
        filters.start_filtering()
        filters.get_filter(filters.FROM_ID_FILTER).fill(10)
        filters.get_filter(filters.TO_ID_FILTER).fill(20)
        filters.get_filter(filters.EMAIL_FILTER).fill('test@test.com')
        filters.get_filter(filters.NAME_FILTER).fill('Test')
        created_at_from_datepicker = filters.get_filter(filters.CREATED_AT_FROM_DATAPICKER)
        created_at_from_datepicker.click()
        created_at_from_datepicker.select_month('Jan')
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
        filters = page.grid_filters
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
        purchase_point = filters.get_filter(filters.PURCHASE_POINT)
        purchase_point.select('Default Store View')
        increment_id = filters.get_filter(filters.INCREMENT_ID)
        increment_id.fill('45577676')
        bill_to_name = filters.get_filter(filters.BILL_TO_NAME)
        bill_to_name.fill('Test')
        ship_to_name = filters.get_filter(filters.SHIP_TO_NAME)
        ship_to_name.fill('Test')
        status = filters.get_filter(filters.STATUS)
        status.select('Canceled')
        braintree_transaction_source = filters.get_filter(filters.BRAINTREE_TRANSACTION_SOURCE)
        braintree_transaction_source.fill('PayPal')
        filters.apply_filters()


@then("I want to be able to click the customers actions button")
def step_impl(context):
    with CustomersGrid() as page:
        page.grid_actions.click_actions_button()


@step("I want to choose the action I want to perform")
def step_impl(context):
    with CustomersGrid() as page:
        page.grid_actions.click_action('Delete')


@step("if I have not selected a grid item")
def step_impl(context):
    pass


@then("I should see a warning modal window")
def step_impl(context):
    with CustomersGrid() as page:
        assert page.browser.is_text_present('Attention')
        assert page.modal.ok_button.is_visible(10) is True
        page.modal.click_ok_button()


@given("I select the first customers grid row")
def step_impl(context):
    with CustomersGrid() as page:
        page.grid_rows.wait_for_spinner()
        page.grid_rows.click_row_checkbox(1, True)


@step("I choose the customers Delete action")
def step_impl(context):
    with CustomersGrid() as page:
        page.grid_actions.click_actions_button()
        page.grid_actions.click_action('Delete')


@then("I should see a confirmation modal window")
def step_impl(context):
    with CustomersGrid() as page:
        assert page.browser.is_text_present('Are you sure you want to delete the selected customers?')
        assert page.modal.cancel_button.is_visible(10) is True


@step("I want to cancel the action")
def step_impl(context):
    with CustomersGrid() as page:
        page.modal.click_cancel_button()


@step("I choose the Cancel action")
def step_impl(context):
    with SalesOrdersGrid() as page:
        page.grid_actions.click_actions_button()
        page.grid_actions.click_action('Cancel')


@step("I choose the Assign a Customer Group action")
def step_impl(context):
    with CustomersGrid() as page:
        page.grid_actions.click_actions_button()
        page.grid_actions.click_action('Assign a Customer Group')


@then("I should see an assign customer to group confirmation dialog")
def step_impl(context):
    with CustomersGrid() as page:
        assert page.grid_actions.submenu_actions_list.root.is_visible(10) is True
        page.grid_actions.click_sub_action('General')
        assert page.browser.is_text_present('Are you sure to assign selected customers to new group?')
        page.modal.click_cancel_button()


@then("I want to select the second sales orders grid row")
def step_impl(context):
    with SalesOrdersGrid() as page:
        page.grid_rows.wait_for_spinner()
        page.grid_rows.click_row_checkbox(2, True)


@given("I am successfully connected to the Magento MariaDB database")
def step_impl(context):
    assert context.conn is not None


@then("I want to be able to execute a select query")
def step_impl(context):
    cur = context.conn.cursor()
    cur.execute("SELECT ccd.value FROM core_config_data ccd WHERE path = ?", ('catalog/search/engine',))
    search_engine = cur.fetchone()[0]
    assert search_engine == 'opensearch'


@then("I want to be able to execute an update query against the test database")
def step_impl(context):
    try:
        cur = context.conn.cursor()
        cur.execute("UPDATE core_config_data ccd SET ccd.value = 'dummy' WHERE ccd.path = 'catalog/search/engine'")
        context.conn.commit()
        cur.execute("SELECT ccd.value FROM core_config_data ccd WHERE path = ?", ('catalog/search/engine', ))
        search_engine = cur.fetchone()[0]
        assert search_engine == 'dummy'
    except mariadb.Error:
        context.conn.rollback()


@step("the environment database data must not have been modified")
def step_impl(context):
    cur = context.conn.cursor()
    cur.execute('USE magento')
    cur.execute("SELECT ccd.value FROM core_config_data ccd WHERE path = ?", ('catalog/search/engine',))
    search_engine = cur.fetchone()[0]
    assert search_engine == 'opensearch'
