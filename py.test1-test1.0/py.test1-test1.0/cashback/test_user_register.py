from pages.register_page import RegisterPage
from pages.main_page import MainPage
from pages.office_page import OfficePage
import pytest
import time

def test_register_user_without_sponsor(browser):
    link = "http://ag.t.ukrtech.info/"
    main_page = MainPage(browser, link)
    register_page = RegisterPage(browser, link)
    office_page = OfficePage(browser, link)
    browser.get(link)
    main_page.open_register_page()
    register_page.fill_user_login()
    register_page.fill_email_field()
    register_page.fill_phone_field()
    register_page.fill_pass_field()
    register_page.click_checkbox()
    register_page.click_register_button()
    office_page.get_alert_message()
