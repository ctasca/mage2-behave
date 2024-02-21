from behave import *


@given(u'I have made an integration admin token request')
def step_impl(context):
    """ Request is made via fixture. There is no need to anything here """
    assert True is not False


@then(u'I expect a successful response')
def step_impl(context):
    assert context.admin_token
