from .base_page import BasePage
from .locators import AccountPageLocators
from .tools.dict_file import DictFile
from faker import Faker
from selenium.webdriver.support.ui import Select

class AccountPage(BasePage):
    def open_edit_form(self):
        edit_form_link = self.browser.find_element(*AccountPageLocators.EDIT_ACCOUNT)
        edit_form_link.click()
