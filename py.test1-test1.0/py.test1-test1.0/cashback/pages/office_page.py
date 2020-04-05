# -*- coding: utf-8 -*-
from .base_page import BasePage
from .locators import OfficePageLocators


class OfficePage(BasePage):
    def get_alert_message(self):
        alert_message = self.browser.find_element(*OfficePageLocators.ALERT_MESSAGE_LOCATOR)
        actual_result = alert_message.text.strip()
        print(actual_result)
        expected_result = "Подтвердите Email-адрес."
        expected_result = expected_result.decode('utf-8')
        print(expected_result)
        assert actual_result.startswith(expected_result)

#TODO создать мапу для хранения данных, что б потом их во время достать и использовать для необходимых действий и входа на юзера (словари)