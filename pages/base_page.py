from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver import Driver

class BasePage(Driver):

    def type(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys()

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def wait_for_element(self, locator, wait_time) -> WebElement:
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_element_located(locator))

    def get_element_text(self, locator):
        return self.wait_for_element(locator, 8).text
