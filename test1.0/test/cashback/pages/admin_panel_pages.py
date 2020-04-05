from .base_page import BasePage
from .locators import AdminPanelLocators
from .tools.dict_file import DictFile

class AdminPage(BasePage):
    dict_file = DictFile()
    def open_mail_page(self):
        mail_page_link = self.browser.find_element(*AdminPanelLocators.MAIL_PAGE_LINK_LOCATOR)
        mail_page_link.click()

    def open_email(self):
        mail_link = self.browser.find_element(*AdminPanelLocators.OPEN_MAIL_LINK_LOCATOR)
        mail_link.click()

    def get_confirm_link(self):
        dict_file = DictFile()
        confirm_link = self.browser.find_element(*AdminPanelLocators.CONFIRM_MAIL_LINK_LOCATOR)
        confirm_link.get_attribute("href")
        dict_file.d['link1'] = confirm_link.get_attribute("href")


