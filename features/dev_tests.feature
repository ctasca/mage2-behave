@fixture.recreate.development.test.db
@fixture.use.development.test.db
@fixture.warden.maria.db.connect
@fixture.integration.admin.token
@fixture.before.cleanup.screenshots
Feature: As a mage2-behave developer I want to test the functionality of my code So That I can assure all is properly working

    @skip
    @browser
    @fixture.splinter.browser.chrome
    Scenario: Browser Chrome fixture test
        Given I visit Google search page
         Then the title should be "Google"

    @skip
    @browser
    @fixture.splinter.browser.chrome.fullscreen
    Scenario: Browser Chrome fixture fullscreen test
        Given I visit Google search page
         Then the title should be "Google"

    @skip
    @browser
    @fixture.splinter.browser.chrome.screen.size.200:200
    Scenario: Browser Chrome custom size screen fixture test
        Given I visit Google search page
         Then the title should be "Google"

    @backend
    @fixture.splinter.browser.chrome.headless
    Scenario: Navigate to Admin Login Page
        Given I am on the admin login page
        Then the title should be "Magento Admin"

    @backend
    @fixture.splinter.browser.chrome.headless
    Scenario: Navigate to Admin Login Page
        Given I am on the admin login page
        When I enter my credentials
        And I sign in
        Then I should see a dashboard header

        @ss
    @backend
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin login and click the Sales menu item
        Given I am logged in the backend
        When I click the "Sales" menu item
        Then I should see the "Sales" submenu links

    @backend
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin login and click the Catalog menu item
        Given I am logged in the backend
        When I click the "Catalog" menu item
        Then I should see the "Catalog" submenu links

    @backend
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin login and click the Customers menu item
        Given I am logged in the backend
        When I click the "Customers" menu item
        Then I should see the "Customers" submenu links

    @backend
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin login and click the Marketing menu item
        Given I am logged in the backend
        When I click the "Marketing" menu item
        Then I should see the "Marketing" submenu links

    @backend
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin login and click the Content menu item
        Given I am logged in the backend
        When I click the "Content" menu item
        Then I should see the "Content" submenu links

    @backend
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin login and click the Reports menu item
        Given I am logged in the backend
        When I click the "Reports" menu item
        Then I should see the "Reports" submenu links

    @backend
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin login and click the Stores menu item
        Given I am logged in the backend
        When I click the "Stores" menu item
        Then I should see the "Stores" submenu links

    @backend
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin login and click the System menu item
        Given I am logged in the backend
        When I click the "System" menu item
        Then I should see the "System" submenu links

    @backend.grid
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin can view the customers grid
        Given I am logged in the backend
        When I want to view all my customers
        Then I should be viewing the customer grid

    @backend
    @store.switcher
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin can change store scope
        Given I am logged in the backend
        When I want to change store scope
        Then I should be able to select the store I want to switch to

    @backend-1
    @backend.grid.filters
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin can view the customers grid and apply filters
        Given I am on the all customers grid
        Then I want to be able to apply filters to customers for searching purposes
        And I want to be able to reset the customers grid applied filters

    @backend
    @backend.grid.actions
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin can view the customers grid and perform actions
        Given I am on the all customers grid
        Then I want to be able to click the customers actions button
        And I want to choose the action I want to perform
        But if I have not selected a grid item
        Then I should see a warning modal window

    @backend
    @backend.grid.rows
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin can view the customers grid, select rows checkboxes and perform actions
        Given I am on the all customers grid
        And I select the first customers grid row
        And I choose the customers Delete action
        Then I should see a confirmation modal window
        And I want to cancel the action

    @backend
    @backend.grid.actions.submenu
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin can view the customers grid and perform actions with a submenu
        Given I am on the all customers grid
        And I select the first customers grid row
        And I choose the Assign a Customer Group action
        Then I should see an assign customer to group confirmation dialog

    @backend
    @backend.grid.search.fulltext
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin can view the customers grid and use the search fulltext input
        Given I am on the all customers grid
        Then I want to be able to use the search fulltext input to filter the grid
        And I want to be able to reset the customers grid applied filters

    @backend
    @backend.grid.rows
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin can view the sales order grid and choose an action
        Given I am on the sales orders grid
        And I choose the Cancel action
        But if I have not selected a grid item
        Then I should see a warning modal window


    @backend
    @backend.grid.rows
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin can view the sales orders grid and select a row in the grid
        Given I am on the sales orders grid
        Then I want to select the second sales orders grid row

    @backend
    @backend.orders.grid.filters
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin can view the sales orders grid and apply filters
       Given I am on the sales orders grid
        Then I want to be able to apply filters to orders for searching purposes
        And I want to be able to reset the sales orders grid applied filters

    @backend
    @backend.dashboard
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin can reload data on the Dashboard page
        Given I am on the backend Dashboard page
        Then I want to be able to reload data

    @backend
    @backend.dashboard
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin can click diagram tabs on Dashboard page
        Given I am on the backend Dashboard page
        Then I want to be able to choose and view the diagram tabs

    @backend
    @backend.dashboard
    @fixture.splinter.browser.chrome.headless
    Scenario: Admin can click store statistics tabs on Dashboard page
        Given I am on the backend Dashboard page
        Then I want to be able to choose and view the store statistics tabs

    @api
    Scenario: Create an amin user integration bearer token
        Given I have made an integration admin token request
        Then I expect a successful response

    @api
    @fixture.dummy.customer.create
    @fixture.dummy.customer.delete
    Scenario: Create a dummy customer via Magento 2 API with admin integration token
        Given I want to create a dummy customer for my tests
        When the request is made
        Then I should have a context dummy customer id

    @api
    @products
    @fixture.set.products.in.stock.WJ12:WJ10
    Scenario: Products stock items are set in stock for each sku given
        Given I have needed products in stock
        Then I should be able to add them to my shopping cart

    @api
    @products
    @fixture.set.products.out.of.stock.WJ12:WJ10
    Scenario: Products stock items are set in stock for each sku given
        Given I have products out of in stock
        Then I should not be able to add them to my shopping cart

    @bin.magento
    Scenario: Configured docker php-fpm service container executes bin/magento commands
        Given I have flushed the magento cache

    @db
    Scenario: I can connect to warden MariaDB
        Given I am successfully connected to the Magento MariaDB database
        Then I want to be able to execute a select query

    @db
    Scenario: I can connect to warden MariaDB test database
        Given I am successfully connected to the Magento MariaDB database
        Then I want to be able to execute an update query against the test database
        And the environment database data must not have been modified
