from behave import *

@given('I on the login page1')
def step_impl(context):
    context.login_page.navigate_to_page()

@when('I insert an username1 "{username}"')
def step_impl(context, username):
    context.login_page.set_email(username)

@when('I insert a password1 "{password}"')
def step_impl(context, password):
    context.login_page.set_password(password)

@when('I click on the login button1')
def step_impl(context):
    context.login_page.click_login()

@then('The banner is displayed1')
def step_impl(context):
    assert context.login_page.is_message_displayed(), 'The succes login'

@then('The login is succes "{message}"')
def step_impl(context, message):
    context.login_page.get_message_text(message)


