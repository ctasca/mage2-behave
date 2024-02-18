from behave import *
from pages.google import Google

@given(u'I visit Google search page')
def step_impl(context):
   with Google() as page:
        page.base_url = 'https://www.google.com/'
        page.navigate()


@then(u'the title should be "{title}"')
def step_impl(context, title):
    assert title in context.browser.title
