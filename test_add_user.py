import self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from AddPage import AddHelpers
from AuthPage import AuthHelpers
from conftest import driver
from webdriver_manager.chrome import ChromeDriverManager
import pytest




class TestAddUser:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.AddPage = AddHelpers(driver)
        self.AuthPage = AuthHelpers(driver)
        self.AddPage.go_to_site()
        self.AuthPage.fill_login_form("test@protei.ru")
        self.AuthPage.fill_password_form("test")
        self.AuthPage.click_auth_button()


    def test_add_user_with_valid_data(self):
        self.AddPage.fill_email_form('abc@mail.ru')
        self.AddPage.fill_name_form('Михаил')
        self.AddPage.fill_gender_form('Мужской')
        self.AddPage.choose_check_box(1)
        self.AddPage.choose_radio_group(3)
        self.AddPage.click_add_button()
        add_message = self.AddPage.get_add_success_message()
        assert "Данные добавлены." == add_message

    def test_add_user_man_with_all_chekcboxes(self):
        self.AddPage.fill_email_form('abc@mail.ru')
        self.AddPage.fill_name_form('Сергей')
        self.AddPage.fill_gender_form('Мужской')
        self.AddPage.choose_check_box(1)
        self.AddPage.choose_check_box(2)
        self.AddPage.choose_radio_group(2)
        self.AddPage.click_add_button()
        add_message = self.AddPage.get_add_success_message()
        assert "Данные добавлены." == add_message

    def test_add_user_woman_with_all_chekcboxes(self):
        self.AddPage.fill_email_form('svet@mailz.ru')
        self.AddPage.fill_name_form('Светлана')
        self.AddPage.fill_gender_form('Женский')
        self.AddPage.choose_check_box(1)
        self.AddPage.choose_check_box(2)
        self.AddPage.choose_radio_group(2)
        self.AddPage.click_add_button()
        add_message = self.AddPage.get_add_success_message()
        assert "Данные добавлены." == add_message

    def test_add_user_zero_name_form(self):
        self.AddPage.fill_email_form('ssdv@mail.ru')
        self.AddPage.fill_name_form('')
        self.AddPage.fill_gender_form('Женский')
        self.AddPage.choose_check_box(2)
        self.AddPage.choose_radio_group(1)
        self.AddPage.click_add_button()
        error_name = self.AddPage.get_error_name_message()
        assert "Поле имя не может быть пустым" == error_name

    def test_add_user_zero_email_form(self):
        self.AddPage.fill_email_form('')
        self.AddPage.fill_name_form('Никита')
        self.AddPage.fill_gender_form('Мужской')
        self.AddPage.choose_check_box(2)
        self.AddPage.choose_radio_group(2)
        self.AddPage.click_add_button()
        error_email = self.AddPage.get_error_email_message()
        assert "Неверный формат E-Mail" == error_email

    def test_add_user_invalid_email_form(self):
        self.AddPage.fill_email_form('@mail.ru')
        self.AddPage.fill_name_form('Екатерина')
        self.AddPage.fill_gender_form('Женский')
        self.AddPage.choose_check_box(1)
        self.AddPage.choose_radio_group(3)
        self.AddPage.click_add_button()
        error_email = self.AddPage.get_error_email_message()
        assert "Неверный формат E-Mail" == error_email

    def test_add_user_without_probel_name_form(self):
        self.AddPage.fill_email_form('czxc@mail.ru')
        self.AddPage.fill_name_form(' Нина ')
        self.AddPage.fill_gender_form('Женский')
        self.AddPage.choose_check_box(1)
        self.AddPage.choose_radio_group(2)
        self.AddPage.click_add_button()
        add_message = self.AddPage.get_add_success_message()
        assert "Данные добавлены." == add_message

    def test_add_user_zero_choose_checkbox(self):
        self.AddPage.fill_email_form('jfscb@mail.ru')
        self.AddPage.fill_name_form('Аркадий')
        self.AddPage.fill_gender_form('Мужской')
        self.AddPage.choose_radio_group(1)
        self.AddPage.click_add_button()
        add_message = self.AddPage.get_add_success_message()
        assert "Данные добавлены." == add_message

    def test_add_user_proof_add_in_table(self):
        self.AddPage.fill_email_form('onebv@mail.ru')
        self.AddPage.fill_name_form('Виктория')
        self.AddPage.fill_gender_form('Женский')
        self.AddPage.choose_check_box(2)
        self.AddPage.choose_radio_group(1)
        self.AddPage.click_add_button()
        self.AddPage.click_ok_button()
        table_email= self.AddPage.get_email_table_row()
        assert 'onebv@mail.ru' == table_email

    def test_add_user_zero_choose_radio_group(self):
        self.AddPage.fill_email_form('zxvjn@mail.ru')
        self.AddPage.fill_name_form('Игорь')
        self.AddPage.fill_gender_form('Мужской')
        self.AddPage.choose_check_box(2)
        self.AddPage.click_add_button()
        add_message = self.AddPage.get_add_success_message()
        assert "Данные добавлены." == add_message

    def test_add_user_zero_choose_radio_group_and_checkbox(self):
        self.AddPage.fill_email_form('nmvbcx@mail.ru')
        self.AddPage.fill_name_form('Татьяна')
        self.AddPage.fill_gender_form('Женский')
        self.AddPage.click_add_button()
        add_message = self.AddPage.get_add_success_message()
        assert "Данные добавлены." == add_message

    def test_add_user_with_min_name_form(self):
        self.AddPage.fill_email_form('reuuqdc@mail.ru')
        self.AddPage.fill_name_form('М')
        self.AddPage.fill_gender_form('Мужской')
        self.AddPage.choose_check_box(1)
        self.AddPage.choose_radio_group(2)
        self.AddPage.click_add_button()
        add_message = self.AddPage.get_add_success_message()
        assert "Данные добавлены." == add_message

