import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("file:///C:/Users/Колобокпиранья/Downloads/Telegram%20Desktop/qa-test.html")
    yield driver
    driver.quit()