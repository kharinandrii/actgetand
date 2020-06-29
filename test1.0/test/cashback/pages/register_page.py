from .base_page import BasePage
from .locators import RegisterPageLocators
from .tools.dict_file import DictFile
from faker import Faker
import time
import random
class RegisterPage(BasePage):
    def fillFirstName(self, name):
        first_name_field = self.browser.find_element(*RegisterPageLocators.FIRST_NAME)
        first_name_field.send_keys(name)

