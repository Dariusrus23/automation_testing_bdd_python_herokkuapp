from behave import *

@given('I on the login page')
def step_impl(context):
    context.login_page.navigate_to_page()

@when('I insert an username1 "{username}"')
def step_impl(context, username):
    context.login_page.set_email(username)

@when('I insert a password2 "{password}"')
def step_impl(context, password):
    context.login_page.set_password(password)

@when('I click on the login button1')
def step_impl(context):
    context.login_page.click_login()

@then('The banner is displayed1')
def step_impl(context):
    assert context.login_page.is_message_displayed(), 'The succes login'

@then('The message is displayd "You logged into a secure area!"')
def step_impl(context):
    try:
        text = context.driver.find_element_by_xpath("//div[@class='button secondary radius']")
    except:
        context.drive.close()
        assert False, "test fail"
    if text=="Logout":
        context.drive.close()
        assert True, "test passed"


