from .base_page import BasePage
from .locators import ProfileLocators
from .tools.dict_file import DictFile

class ProfilePage(BasePage):

    def check_name(self):
        name_field = self.browser.find_element(*ProfileLocators.NAME_LOCATOR)
        actual_result = name_field.get_attribute('value')
        expected_result = DictFile.register_form_dict["name"]
        assert actual_result == expected_result

    def check_lastname(self):
        last_name_field = self.browser.find_element(*ProfileLocators.LASTNAME_LOCATOR)
        actual_result = last_name_field.get_attribute('value')
        expected_result = DictFile.register_form_dict["lastname"]
        assert actual_result == expected_result

    def check_email(self):
        email_field = self.browser.find_element(*ProfileLocators.EMAIL_LOCATOR)
        actual_result = email_field.get_attribute('value')
        expected_result = DictFile.register_form_dict["email"]
        assert actual_result == expected_result

    def check_phone(self):
        phone_field = self.browser.find_element(*ProfileLocators.PHONE_LOCATOR)
        actual_result = phone_field.get_attribute('value')
        expected_result = DictFile.register_form_dict["phone"]
        assert actual_result == expected_result

    def open_next_page(self):
        continue_button = self.browser.find_element(*ProfileLocators.CONTINUE_BUTTON)
        continue_button.click()

    def check_profile_page(self):
        self.check_name()
        self.check_lastname()
        self.check_email()
        self.check_phone()
        self.open_next_page()
