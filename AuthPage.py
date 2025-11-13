from AddPage import AddLocators
from BasePage import BasePage
from selenium.webdriver.common.by import By

class AuthLocators:
    LOCATOR_LOGIN_INPUT = (By.XPATH, "//input[@id='loginEmail']")
    LOCATOR_PASSWORD_INPUT = (By.XPATH, "//input[@id='loginPassword']")
    LOCATOR_AUTH_BUTTON = (By.XPATH, "//button[@id='authButton']")
    LOCATOR_ERROR_MESSAGE = (By.XPATH, "//div[@id='emailFormatError']")
    LOCATOR_INVALID_EMAIL = (By.XPATH, "//div[@id='invalidEmailPassword']")



class AuthHelpers(BasePage):
    def fill_login_form(self, login):
        login_input = self.find_element(AuthLocators.LOCATOR_LOGIN_INPUT)
        login_input.send_keys(login)

    def fill_password_form(self, password):
        password_input = self.find_element(AuthLocators.LOCATOR_PASSWORD_INPUT)
        password_input.send_keys(password)

    def click_auth_button(self):
        button = self.find_element(AuthLocators.LOCATOR_AUTH_BUTTON)
        button.click()

    def get_error_message(self):
        error_message = self.find_element(AuthLocators.LOCATOR_ERROR_MESSAGE)
        return error_message

    def get_invalid_email(self):
        invalid_email = self.find_element(AuthLocators.LOCATOR_INVALID_EMAIL)
        return invalid_email

    def get_send_data_button_text(self):
        data_send = self.find_element(AddLocators.LOCATOR_ADD_BUTTON)
        return data_send.text
