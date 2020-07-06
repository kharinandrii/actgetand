from .pages.main_page import MainPageOpenCard
from .pages.register_page import RegisterPage
from .pages.success_page import SuccessPage
from .pages.account_page import AccountPage
from .pages.profile_page import ProfilePage
import time

def test_main_page(browser):
    link = 'http://opencart.abstracta.us/'

    main_page = MainPageOpenCard(browser, link)
    success_page = SuccessPage(browser, link)
    account_page = AccountPage(browser, link)
    profile_page = ProfilePage(browser, link)

    browser.get(link)

    main_page.open_register_page()
    main_page.click_on_register_link()
    main_page.save_page_click()

    register_page = RegisterPage(browser, link)
    register_page.fill_first_name()
    register_page.fill_last_name()
    register_page.fill_email()
    register_page.fill_phone()
    register_page.fill_address()
    register_page.fill_city("Kherson")
    register_page.fill_postcode("73020")
    register_page.choose_country('220')
    register_page.choose_region("3494")
    register_page.fill_password('123456t')
    register_page.fill_password_confirm('123456t')
    register_page.click_on_checkbox()
    register_page.click_on_continue_button()
    success_page.check_success_message('Your Account Has Been Created!')
    success_page.click_on_continue()
    account_page.open_edit_form()
    profile_page.check_profile_page()
    time.sleep(20000)



