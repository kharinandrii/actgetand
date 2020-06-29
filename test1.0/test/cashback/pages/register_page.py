from .base_page import BasePage
from .locators import RegisterPageLocators
from .tools.dict_file import DictFile
from faker import Faker
import time
import random
class RegisterPage(BasePage):
    def fill_first_name(self, name):
        first_name_field = self.browser.find_element(*RegisterPageLocators.FIRST_NAME)
        first_name_field.send_keys(name)

    def fill_last_name(self, last_name):
        last_name_field = self.browser.find_element(*RegisterPageLocators.LAST_NAME)
        last_name_field.send_keys(last_name)

    def fill_email(self, mail):
        email_field = self.browser.find_element(*RegisterPageLocators.EMAIL)
        email_field.send_keys(mail)

    def fill_phone(self, phone):
        phone_field = self.browser.find_element(*RegisterPageLocators.PHONE)
        phone_field.send_keys(phone)

    def fill_address(self, address):
        address_field = self.browser.find_element(*RegisterPageLocators.ADDRESS)
        address_field.send_keys(address)




