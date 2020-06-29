from .pages.main_page import MainPageOpenCard
from .pages.register_page import RegisterPage
from faker import Faker
import time
def test_main_page(browser):
    link = 'http://opencart.abstracta.us/'
    faker = Faker()
    name = faker.first_name()
    last_name = faker.last_name()
    mail = last_name + "@test.com"
    phone = str(time.time()).replace('.', '')
    address = faker.address()
    main_page = MainPageOpenCard(browser, link)

    browser.get(link)

    main_page.open_register_page()
    main_page.click_on_register_link()
    main_page.save_page_click()

    register_page = RegisterPage(browser, link)
    register_page.fill_first_name(name)
    register_page.fill_last_name(last_name)
    register_page.fill_email(mail)
    register_page.fill_phone(phone)
    register_page.fill_address(address)
    register_page.fill_city("Kherson")
    register_page.fill_postcode("73020")
    register_page.choose_country('220')
    register_page.choose_region("3494")
    register_page.fill_password('123456t')
    register_page.fill_password_confirm('123456t')
    register_page.click_on_continue_button()


    time.sleep(20000)



