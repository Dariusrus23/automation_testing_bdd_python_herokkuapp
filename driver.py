from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:

    chrome_options = Options()
    chrome_options.add_argument("--disable-notrifications")
    driver = webdriver.Chrome(options=chrome_options)

    def close(self):
        self.driver.quit()