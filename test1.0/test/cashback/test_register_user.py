from .pages.register_page import RegisterPage
from faker import Faker

def test_create_user(browser):

    link = 'https://opencart.abstracta.us/index.php?route=account/register'
    register_page = RegisterPage(browser, link)
    faker = Faker()
    name = faker.name
    browser.get(link)
    register_page.fillFirstName(name)