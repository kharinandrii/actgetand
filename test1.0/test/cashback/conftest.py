import pytest
from selenium import webdriver
from selenium.webdriver.chrome import options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.close()