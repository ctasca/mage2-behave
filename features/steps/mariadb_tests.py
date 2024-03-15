import mariadb
from behave import *


@given("I am successfully connected to the Magento MariaDB database")
def step_impl(context):
    assert context.conn is not None


@then("I want to be able to execute a select query")
def step_impl(context):
    cur = context.conn.cursor()
    cur.execute("SELECT ccd.value FROM core_config_data ccd WHERE path = ?", ('catalog/search/engine',))
    search_engine = cur.fetchone()[0]
    try:
        if context.keep_test_db:
            assert search_engine == 'dummy'
    except AssertionError:
        assert search_engine == 'opensearch'


@then("I want to be able to execute an update query against the test database")
def step_impl(context):
    try:
        cur = context.conn.cursor()
        cur.execute("UPDATE core_config_data ccd SET ccd.value = 'dummy' WHERE ccd.path = 'catalog/search/engine'")
        context.conn.commit()
        cur.execute("SELECT ccd.value FROM core_config_data ccd WHERE path = ?", ('catalog/search/engine',))
        search_engine = cur.fetchone()[0]
        assert search_engine == 'dummy'
    except mariadb.Error:
        context.conn.rollback()


@step("the environment database data must not have been modified")
def step_impl(context):
    cur = context.conn.cursor()
    cur.execute('USE {}'.format(context.db_name))
    cur.execute("SELECT ccd.value FROM core_config_data ccd WHERE path = ?", ('catalog/search/engine',))
    search_engine = cur.fetchone()[0]
    assert search_engine == 'opensearch'
