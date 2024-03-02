import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchProduct(BasePage):

    MAIN_URL = "https://www.libris.ro/"
    SEARCH_INPUT_SELECTOR = (By.ID, "autoComplete")
    TITLE_SELECTOR = (By.CSS_SELECTOR, "d-none d-md-block pr-description-sec-ct")
    SEARCH_BUTTON_CLICK = (By.CSS_SELECTOR,"div.autoComplete_wrapper > input.onSearchClick" )

    def navigate_to_page(self):
        self.driver.get(self.MAIN_URL)

    def click_on_search_button(self):
        self.click(self.SEARCH_INPUT_SELECTOR)

    def click_on_magnifier_button(self):
        self.click(self.SEARCH_BUTTON_CLICK)

    def type_anything_on_search(self, text_to_search):
        self.type(self.SEARCH_INPUT_SELECTOR, text_to_search)

    def get_title_text(self, expected_text):
        text = self.get_element_text(self.TITLE_SELECTOR)
        assert expected_text in text, f'Expected text:{expected_text},actual text: {text}'