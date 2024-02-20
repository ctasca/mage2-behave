@fixture.integration.admin.token
Feature: As a mage2-behave developer I want to test the funcionality of my code So That I can assure all is properly working

@browser
@fixture.splinter.browser.chrome
Scenario: Browser Chrome fixture test
    Given I visit Google search page
     Then the title should be "Google"

@browser
@fixture.splinter.browser.chrome.fullscreen
Scenario: Browser Chrome fixture test
    Given I visit Google search page
     Then the title should be "Google"

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

@backend
@fixture.splinter.browser.chrome.headless
Scenario: Admin login and perform clicks in admin menu
    Given I am logged in the backend
    When I click the "Sales" menu item
    Then I should see the "Sales" submenu links

@backend
@fixture.splinter.browser.chrome.headless
Scenario: Admin login and perform clicks in admin menu
    Given I am logged in the backend
    When I click the "Catalog" menu item
    Then I should see the "Catalog" submenu links

@backend
@fixture.splinter.browser.chrome.headless
Scenario: Admin login and perform clicks in admin menu
    Given I am logged in the backend
    When I click the "Customers" menu item
    Then I should see the "Customers" submenu links

@backend
@fixture.splinter.browser.chrome.headless
Scenario: Admin login and perform clicks in admin menu
    Given I am logged in the backend
    When I click the "Marketing" menu item
    Then I should see the "Marketing" submenu links

@backend
@fixture.splinter.browser.chrome.headless
Scenario: Admin login and perform clicks in admin menu
    Given I am logged in the backend
    When I click the "Content" menu item
    Then I should see the "Content" submenu links

@backend
@fixture.splinter.browser.chrome.headless
Scenario: Admin login and perform clicks in admin menu
    Given I am logged in the backend
    When I click the "Reports" menu item
    Then I should see the "Reports" submenu links

@backend.grid
@fixture.splinter.browser.chrome
Scenario: Admin can view the customers grid
    Given I am logged in the backend
    When I want to view all my customers 
    Then I should be viewing the customer grid

@backend.grid.filters
@fixture.splinter.browser.chrome
Scenario: Admin can view the customers grid and click the filters button
    Given I am logged in the backend
    When I am on the all customers grid
    Then I want to be able to apply filters for searching purposes

@api
Scenario: Create an integration admin token
    Given I have made an integration admin token request
    Then I expect a successful response