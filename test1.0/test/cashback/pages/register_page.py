from .base_page import BasePage
from .locators import RegisterPageLocators
from .tools.dict_file import DictFile
from faker import Faker
from selenium.webdriver.support.ui import Select
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

    def fill_city(self, city):
        city_field = self.browser.find_element(*RegisterPageLocators.CITY)
        city_field.send_keys(city)

    def fill_postcode(self, postcode):
        postcode_field = self.browser.find_element(*RegisterPageLocators.POSTCODE)
        postcode_field.send_keys(postcode)

    def choose_country(self, value):
        country_select = Select(self.browser.find_element(*RegisterPageLocators.COUNTRY))
        country_select.select_by_value(value)



