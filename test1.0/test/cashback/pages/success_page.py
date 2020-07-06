from .base_page import BasePage
from .locators import SuccessPageLocators

class SuccessPage(BasePage):

    def check_success_message(self, expected_result):
        success_message = self.browser.find_element(*SuccessPageLocators.SUCCESS_MESSAGE)
        actual_result = success_message.text
        assert actual_result == expected_result

    def click_on_continue(self):
        continue_button = self.browser.find_element(*SuccessPageLocators.CONTINUE_BUTTON)
        continue_button.click()
