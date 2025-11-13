import self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from AuthPage import AuthHelpers
from conftest import driver
from webdriver_manager.chrome import ChromeDriverManager
import pytest




class TestAuth:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.AuthPage = AuthHelpers(driver)
        self.AuthPage.go_to_site()


    def test_valid_login_and_password(self):
        self.AuthPage.fill_login_form("test@protei.ru")
        self.AuthPage.fill_password_form("test")
        self.AuthPage.click_auth_button()
        button_auth = self.AuthPage.get_send_data_button_text()
        assert "Добавить" == button_auth

    def test_zero_data_and_password(self):
        self.AuthPage.fill_login_form("")
        self.AuthPage.fill_password_form("")
        self.AuthPage.click_auth_button()
        error_message = self.AuthPage.get_error_message()
        assert "Неверный формат E-Mail" == error_message.text

    def test_zero_password_valid_email(self):
        self.AuthPage.fill_login_form("test@protei.ru")
        self.AuthPage.fill_password_form("")
        self.AuthPage.click_auth_button()
        invalid_email = self.AuthPage.get_invalid_email()
        assert "Неверный E-Mail или пароль" == invalid_email.text

    def test_zero_data_valid_password(self):
        self.AuthPage.fill_login_form("")
        self.AuthPage.fill_password_form("test")
        self.AuthPage.click_auth_button()
        error_message = self.AuthPage.get_error_message()
        assert "Неверный формат E-Mail" == error_message.text

    def test_valid_data_invalid_password(self):
        self.AuthPage.fill_login_form("test@protei.ru")
        self.AuthPage.fill_password_form("zxcv")
        self.AuthPage.click_auth_button()
        invalid_email = self.AuthPage.get_invalid_email()
        assert "Неверный E-Mail или пароль" == invalid_email.text

    def test_invalid_data_valid_password(self):
        self.AuthPage.fill_login_form("boods@pratei.ge")
        self.AuthPage.fill_password_form("test")
        self.AuthPage.click_auth_button()
        invalid_email = self.AuthPage.get_invalid_email()
        assert "Неверный E-Mail или пароль" == invalid_email.text

    def test_kiriliza_data_valid_password(self):
        self.AuthPage.fill_login_form("тест@протей.ру")
        self.AuthPage.fill_password_form("test")
        self.AuthPage.click_auth_button()
        invalid_email = self.AuthPage.get_invalid_email()
        assert "Неверный E-Mail или пароль" == invalid_email.text

    def test_invalid_format_data_valid_password(self):
        self.AuthPage.fill_login_form("testprotei.ru")
        self.AuthPage.fill_password_form("test")
        self.AuthPage.click_auth_button()
        error_message = self.AuthPage.get_error_message()
        assert "Неверный формат E-Mail" == error_message.text

    def test_min_vormat_data_valid_password(self):
        self.AuthPage.fill_login_form("@protei.ru")
        self.AuthPage.fill_password_form("test")
        self.AuthPage.click_auth_button()
        error_message = self.AuthPage.get_error_message()
        assert "Неверный формат E-Mail" == error_message.text

    def test_spez_sim_data_valid_password(self):
        self.AuthPage.fill_login_form("!test@protei.ru")
        self.AuthPage.fill_password_form("test")
        self.AuthPage.click_auth_button()
        invalid_email = self.AuthPage.get_invalid_email()
        assert "Неверный E-Mail или пароль" == invalid_email.text

    def test_valid_data_probel_password(self):
        self.AuthPage.fill_login_form("!test@protei.ru")
        self.AuthPage.fill_password_form("test ")
        self.AuthPage.click_auth_button()
        invalid_email = self.AuthPage.get_invalid_email()
        assert "Неверный E-Mail или пароль" == invalid_email.text



