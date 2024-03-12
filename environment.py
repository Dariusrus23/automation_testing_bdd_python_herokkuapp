from browser import Browser
from pages.login_page import LoginPage
from pages.emag_search_page import EmagSearchPage

def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.emag_search = EmagSearchPage()

def after_all(context):
    context.browser.close()