from behave import *

@given(u'I have made an integration admin token request')
def step_impl(context):
    assert True is not False


@then(u'I expect a successful response')
def step_impl(context):
    assert context.admin_token
