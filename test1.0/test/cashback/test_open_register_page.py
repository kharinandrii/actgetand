from .pages.main_page import MainPageOpenCard
from .pages.register_page import RegisterPage
from faker import Faker

def test_main_page(browser):
    link = 'http://opencart.abstracta.us/'
    main_page = MainPageOpenCard(browser, link)
    browser.get(link)
    main_page.open_register_page()
    main_page.click_on_register_link()
    main_page.save_page_click()
    register_page = RegisterPage(browser, link)
    faker = Faker()
    name = faker.name()
    register_page.fillFirstName(name)

