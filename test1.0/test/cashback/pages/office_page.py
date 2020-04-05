# -*- coding: utf-8 -*-
from .base_page import BasePage
from .locators import OfficePageLocators


class OfficePage(BasePage):
    def get_alert_message(self):
        alert_message = self.browser.find_element(*OfficePageLocators.ALERT_MESSAGE_LOCATOR)
        actual_result = alert_message.text.strip()
        expected_result = "Подтвердите Email-адрес."
        expected_result = expected_result
        assert actual_result.startswith(expected_result)

#TODO создать мапу для хранения данных, что б потом их во время достать и использовать для необходимых действий и входа на юзера (словари)

    def open_admin_panel(self):
        admin_panel_link = self.browser.find_element(*OfficePageLocators.ADMIN_PANEL_LINK_LOCATOR)
        admin_panel_link.click()

    def user_logout(self):
        logout_link = self.browser.find_element(*OfficePageLocators.LOGOUT_LINK_LOCATOR)
        logout_link.click()

    def check_user_confirm(self):
        confirm_message = self.browser.find_element(*OfficePageLocators.SUCCES_ALERT_LOCATOR)
        actual_result = confirm_message.text.strip()
        expected_result = "Email подтверждён."
        assert actual_result == expected_result