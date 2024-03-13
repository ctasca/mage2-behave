Feature: As a developer I want to be able to run queries against the test database So That the Magento 2 database won't be modified
    @db
    Scenario: I can connect to warden MariaDB
        Given I am successfully connected to the Magento MariaDB database
        Then I want to be able to execute a select query

    @db
    Scenario: I can connect to warden MariaDB test database
        Given I am successfully connected to the Magento MariaDB database
        Then I want to be able to execute an update query against the test database
        And the environment database data must not have been modified
