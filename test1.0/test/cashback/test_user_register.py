from .pages.register_page import RegisterPage
from .pages.main_page import MainPage
from .pages.office_page import OfficePage
from .pages.login_page import LoginPage
import time
from .pages.admin_panel_pages import AdminPage
from .pages.tools.dict_file import DictFile
def test_register_user_without_sponsor(browser):
    link = "http://ag.t.ukrtech.info/"
    main_page = MainPage(browser, link)
    register_page = RegisterPage(browser, link)
    office_page = OfficePage(browser, link)
    login_page = LoginPage(browser, link)
    admin_page = AdminPage(browser, link)
    dict_file = DictFile()
    browser.get(link)
    main_page.open_register_page()
    register_page.fill_user_login()
    register_page.fill_email_field()
    register_page.fill_phone_field()
    register_page.fill_pass_field()
    register_page.click_checkbox()
    register_page.click_register_button()
    office_page.get_alert_message()
    office_page.user_logout()
    main_page.open_login_page()
    login_page.get_login_field("admin")
    login_page.get_pass_field("123456q")
    login_page.click_auth_button()
    office_page.open_admin_panel()
    admin_page.open_mail_page()
    admin_page.open_email()
    admin_page.get_confirm_link()
    browser.get(link + "/site/logout")
    browser.get(dict_file.d["link1"])
    login_page.get_login_field(dict_file.d["nameUser"])
    login_page.get_pass_field("123456t")
    login_page.click_auth_button()
    office_page.check_user_confirm()



