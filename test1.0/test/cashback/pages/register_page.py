from .base_page import BasePage
from .locators import RegisterPageLocators
from selenium.webdriver.support.ui import Select
from .tools.dict_file import DictFile
from faker import Faker
import time

class RegisterPage(BasePage):


    def fill_first_name(self):
        name = Faker().first_name()
        first_name_field = self.browser.find_element(*RegisterPageLocators.FIRST_NAME)
        first_name_field.send_keys(name)
        DictFile.register_form_dict["name"] = name




    def fill_last_name(self):
        last_name = Faker().last_name()
        last_name_field = self.browser.find_element(*RegisterPageLocators.LAST_NAME)
        last_name_field.send_keys(last_name)
        DictFile.register_form_dict["lastname"] = last_name

    def fill_email(self):
        mail = DictFile.register_form_dict["lastname"] + "@test.com"
        email_field = self.browser.find_element(*RegisterPageLocators.EMAIL)
        email_field.send_keys(mail)
        DictFile.register_form_dict["email"] = mail

    def fill_phone(self):
        phone = str(time.time()).replace('.', '')
        phone_field = self.browser.find_element(*RegisterPageLocators.PHONE)
        phone_field.send_keys(phone)
        DictFile.register_form_dict["phone"] = phone

    def fill_address(self):
        address = Faker().address()
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

    def choose_region(self, value):
        region_select = Select(self.browser.find_element(*RegisterPageLocators.REGION))
        region_select.select_by_value(value)

    def fill_password(self, password):
        password_field = self.browser.find_element(*RegisterPageLocators.PASSWORD)
        password_field.send_keys(password)

    def fill_password_confirm(self, password):
        password_field = self.browser.find_element(*RegisterPageLocators.PASSWORD_CONFIRM)
        password_field.send_keys(password)

    def click_on_checkbox(self):
        checkbox = self.browser.find_element(*RegisterPageLocators.CHECKBOX)
        checkbox.click()

    def click_on_continue_button(self):
        continue_button = self.browser.find_element(*RegisterPageLocators.CONTINUE_BUTTON)
        continue_button.click()


