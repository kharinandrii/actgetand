from pages.login_page import LoginPage
from pages.main_page import MainPage
import pytest

def test_login_admin(browser):
    link = "http://ag.t.ukrtech.info/"
    login_page = LoginPage(browser, link)
    main_page = MainPage(browser, link)
    browser.get(link)
    main_page.open_login_page()
    login_page.get_login_field("admin")
    login_page.get_pass_field("123456q")
    login_page.click_auth_button()

