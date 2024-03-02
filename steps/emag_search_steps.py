from behave import *

@given('I am on the home page')
def step_impl(context):
    context.emag_search.navigate_to_page()

@when('I click on the search box')
def step_impl(context):
    context.emag_search.click_on_search_button()

@when('I enter the keyword "{keyword}"')
def step_impl(context, keyword):
    context.emag_search.type_anything_on_search(keyword)

@when('I click the magnifier icon')
def step_impl(context):
    context.emag_search.click_on_magnifier_button()

@then('"{keyword}" keyword is in title phrasing element')
def step_impl(context, keyword):
   assert keyword in context.emag_search.get_title_text(), f"{keyword} is not found in title phrasing after search"

#@then('"{message}" keyword is in title phrasing element')
#def step_impl(context, message):
#    context.emag_search_page.get_message_text(message)
