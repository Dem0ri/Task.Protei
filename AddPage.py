from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddLocators(BasePage):
    LOCATOR_EMAIL_INPUT = (By.XPATH, "//input[@id='dataEmail']")
    LOCATOR_NAME_INPUT = (By.XPATH, "//input[@id='dataName']")
    LOCATOR_GENDER_INPUT = (By.XPATH, "//select[@id='dataGender']")
    LOCATOR_CHECKBOX1_INPUT = (By.XPATH, "//input[@id='dataCheck11']")
    LOCATOR_CHECKBOX2_INPUT = (By.XPATH, "//input[@id='dataCheck12']")
    LOCATOR_RADIOGROUP1_INPUT = (By.XPATH, "//input[@id='dataSelect21']")
    LOCATOR_RADIOGROUP2_INPUT = (By.XPATH, "//input[@id='dataSelect22']")
    LOCATOR_RADIOGROUP3_INPUT = (By.XPATH, "//input[@id='dataSelect23']")
    LOCATOR_ADD_BUTTON = (By.XPATH, "//button[@id='dataSend']")
    LOCATOR_ERROR_NAME_MESSAGE = (By.XPATH, "//div[@id='blankNameError']")
    LOCATOR_ERROR_EMAIL_MESSAGE = (By.XPATH, "//div[@id='emailFormatError']")
    LOCATOR_ADD_SUCCESS_MESSAGE = (By.XPATH, "//div[@class='uk-margin uk-modal-content']")
    LOCATOR_OK_BUTTON = (By.XPATH, "//button[text()='Ok']")
    LOCATOR_EMAIL_TABLE_ROW = (By.XPATH, "//table[@id='dataTable']/tbody/tr[1]/td[1]")

class AddHelpers(BasePage):
    def fill_email_form(self, email):
        email_input = self.find_element(AddLocators.LOCATOR_EMAIL_INPUT)
        email_input.send_keys(email)

    def fill_name_form(self, name):
        name_input = self.find_element(AddLocators.LOCATOR_NAME_INPUT)
        name_input.send_keys(name)

    def fill_gender_form(self, gender):
        gender_input = self.find_element(AddLocators.LOCATOR_GENDER_INPUT)
        select = Select(gender_input)
        select.select_by_visible_text(gender)

    def choose_check_box(self, check_box_number):
        match check_box_number:
            case 1:
                check_box1 = self.find_element(AddLocators.LOCATOR_CHECKBOX1_INPUT)
                check_box1.click()
            case 2:
                check_box2 = self.find_element(AddLocators.LOCATOR_CHECKBOX2_INPUT)
                check_box2.click()



    def choose_radio_group(self, radio_group_number):
        match radio_group_number:
            case 1:
                radiogroup1 = self.find_element(AddLocators.LOCATOR_RADIOGROUP1_INPUT)
                radiogroup1.click()
            case 2:
                radiogroup2 = self.find_element(AddLocators.LOCATOR_RADIOGROUP2_INPUT)
                radiogroup2.click()
            case 3:
                radiogroup3 = self.find_element(AddLocators.LOCATOR_RADIOGROUP3_INPUT)
                radiogroup3.click()

    def click_add_button(self):
        button = self.find_element(AddLocators.LOCATOR_ADD_BUTTON)
        button.click()

    def get_error_name_message(self):
        error_name_message = self.find_element(AddLocators.LOCATOR_ERROR_NAME_MESSAGE)
        return error_name_message.get_attribute("textContent")

    def get_error_email_message(self):
        error_email_message = self.find_element(AddLocators.LOCATOR_ERROR_EMAIL_MESSAGE)
        return error_email_message.get_attribute("textContent")

    def get_add_success_message(self):
        add_success_message = self.find_element(AddLocators.LOCATOR_ADD_SUCCESS_MESSAGE)
        return add_success_message.get_attribute("textContent")

    def click_ok_button(self):
        ok_button = self.find_element(AddLocators.LOCATOR_OK_BUTTON)
        ok_button.click()

    def get_email_table_row(self):
        email_table_row = self.find_element(AddLocators.LOCATOR_EMAIL_TABLE_ROW)
        return email_table_row.text



