from .base_page import BasePage
from .locators import SuccessPageLocators

class SuccessPage(BasePage):

    def check_success_message(self, expected_result):
        success_message = self.browser.find_element(*SuccessPageLocators.SUCCESS_MESSAGE)
        actual_result = success_message.text
        print(actual_result)
        assert actual_result == expected_result
        #Todo разобраться с преобразованием строк что б они были в одном регистре