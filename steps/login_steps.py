from behave import *

@given('I am on the login page')
def step_impl(context):
    context.login_page.navigate_to_page()

@when('I insert an username "{username}"')
def step_impl(context, username):
    context.login_page.set_email(username)

@when('I insert a password "{password}"')
def step_impl(context, password):
    context.login_page.set_password(password)

@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login()

@then('The banner is displayed')
def step_impl(context):
    context.login_page.banner_is_displayed()

@then('The message is "{message}"')
def step_impl(context, message):
    context.login_page.check_message_text(message)

@then('The message is displayed')
def step_impl(context):
    context.login_page.message_is_displayed()



