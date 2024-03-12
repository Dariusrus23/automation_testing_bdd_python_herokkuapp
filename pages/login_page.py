import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://the-internet.herokuapp.com/login"
    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "fa-sign-in")
    MESSAGE = (By.ID, "flash")
    BANNER = (By.ID, "flash-messages")

    def navigate_to_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, email):
        #se mai putea scrie si self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.type(self.EMAIL_INPUT, email)

    def set_password(self, password):
        #se mai putea scrie si self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def banner_is_displayed(self):
        self.is_element_displayed(self.BANNER)

    def message_is_displayed(self):
        self.is_element_displayed(self.MESSAGE)

    def check_message_text(self, expected_message):
        text = self.get_element_text(self.MESSAGE)
        assert expected_message in text, f'Expected message:{expected_message}, actual message{text}'

