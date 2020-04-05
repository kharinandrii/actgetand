from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):

    def open_login_page(self):
        login_page_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK_LOCATOR)
        login_page_link.click()

    def open_register_page(self):
        register_page_link = self.browser.find_element(*MainPageLocators.REGISTER_LINK_LOCATOR)
        register_page_link.click()