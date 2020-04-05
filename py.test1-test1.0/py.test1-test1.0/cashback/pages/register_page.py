from .base_page import BasePage
from .locators import RegisterPageLocators
from faker import Faker
import time
import random
class RegisterPage(BasePage):

    def fill_user_login(self):
        login_field = self.browser.find_element(*RegisterPageLocators.USER_LOGIN_LOCATOR)
        fake = Faker()
        user_login = fake.word() + str(random.randint(1, 1000))
        login_field.send_keys(user_login)

    def fill_email_field(self):
        email_field = self.browser.find_element(*RegisterPageLocators.EMAIL_FIELD_LOCATOR)
        email = str(time.time()) + "@fakemail.org"
        email_field.send_keys(email)

    def fill_phone_field(self):
        phone_field = self.browser.find_element(*RegisterPageLocators.PHONE_FIELD_LOCATOR)
        phone_field.clear()
        phone = ("38095" + str(random.randint(1000000, 9999999)))
        phone_field.send_keys(phone)

    def fill_pass_field(self, password="123456t"):
        password_field = self.browser.find_element(*RegisterPageLocators.PASS_FIELD_LOCATOR)
        password_field.send_keys(password)

    def click_checkbox(self):
        checkbox = self.browser.find_element(*RegisterPageLocators.CHEKCBOX_LOCATOR)
        checkbox.click()

    def click_register_button(self):
        register_button =self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON_LOCATOR)
        register_button.click()
