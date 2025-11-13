from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "file:///C:/Users/Колобокпиранья/Downloads/Telegram%20Desktop/qa-test.html"

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator)
        )

    def go_to_site(self):
        return self.driver.get(self.base_url)