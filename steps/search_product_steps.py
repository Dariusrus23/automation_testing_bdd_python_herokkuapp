from behave import *

@given('I am on the main page')
def step_impl(context):
    context.search_product.navigate_to_page()

@when('I click on the search button')
def step_impl(context):
    context.search_product.click_on_search_button()

@when('I enter this name product "{item}"')
def step_impl(context, item):
    context.search_product.type_anything_on_search(item)

@when('I click the magnifier')
def step_impl(context):
    context.search_product.click_on_search_button()

@then('The product "{itemtitle}"')
def step_impl(context, itemtitle):
    context.search_product_page.get_title_text(itemtitle)


