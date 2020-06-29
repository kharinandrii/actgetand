from .base_page import BasePage
from .locators import MainPageLocators
from .locators import SavePageLocators

class MainPageOpenCard(BasePage):

    def open_register_page(self):
        my_account = self.browser.find_element(*MainPageLocators.MY_ACCOUNT_DROBDOWN)
        my_account.click()

    def click_on_register_link(self):
        register_link = self.browser.find_element(*MainPageLocators.REGISTER_LINK)
        register_link.click()
        self.browser.get('https://opencart.abstracta.us/index.php?route=account/register')


    def save_page_click(self):
        details_button = self.browser.find_element(*SavePageLocators.DETAIL_BUTTON)
        details_button.click()
        proceed_link = self.browser.find_element(*SavePageLocators.PROCESS_LINK)
        proceed_link.click()
        # time.sleep(20000)




