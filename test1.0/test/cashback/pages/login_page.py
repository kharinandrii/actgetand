from .base_page import BasePage
from .locators import LoginPageLocators
class LoginPage(BasePage):

    def get_login_field(self, login):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD_LOCATOR)
        login_field.send_keys(login)

    def get_pass_field(self, password):
        password_field = self.browser.find_element(*LoginPageLocators.PASS_FIELD_LOCATOR)
        password_field.send_keys(password)

    def click_auth_button(self):
        auth_button = self.browser.find_element(*LoginPageLocators.AUTH_BUTTON)
        auth_button.click()

