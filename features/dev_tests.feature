@fixture.integration.admin.token
Feature: As a mage2-behave developer I want to test the funcionality of my code So That I can assure all is properly working

@fixture.splinter.browser.chrome
Scenario: Browser Chrome fixture test
    Given I visit Google search page
     Then the title should be "Google"

@fixture.splinter.browser.chrome.fullscreen
Scenario: Browser Chrome fixture test
    Given I visit Google search page
     Then the title should be "Google"

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

@do
Scenario: Create an integration admin token
    Given I have made an integration admin token request
    Then I expect a successful response