from selenium.webdriver.common.by import By

class MainPageLocators():
    MY_ACCOUNT_DROBDOWN =  (By.XPATH, '//*[@class = "list-inline"]//*[text()="My Account"]')
    REGISTER_LINK = (By.XPATH, '//*[text()="Register"]')

class SavePageLocators():
    DETAIL_BUTTON = (By.XPATH, '//*[@id = "details-button"]')
    PROCESS_LINK = (By.XPATH, '//*[@id = "proceed-link"]')

class RegisterPageLocators():
    FIRST_NAME = (By.XPATH, '//*[@id = "input-firstname"]')
    LAST_NAME = (By.XPATH, '//*[@id = "input-lastname"]')
    EMAIL = (By.XPATH, '//*[@id = "input-email"]')
    PHONE = (By.XPATH, '//*[@id = "input-telephone"]')
    ADDRESS = (By.XPATH,'//*[@id = "input-address-1"]')
    CITY = (By.XPATH, '//*[@id  ="input-city"]')
    POSTCODE = (By.XPATH, '//*[@id  ="input-postcode"]')
    COUNTRY = (By.XPATH, '//*[@id = "input-country"]')
    REGION = (By.XPATH, '//*[@id = "input-zone"]')
    PASSWORD = (By.XPATH, '//*[@id = "input-password"]')
    PASSWORD_CONFIRM = (By.XPATH, '//*[@id = "input-confirm"]')
    CHECKBOX = (By.XPATH, '//*[@name = "agree"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@type = "submit"]')

class SuccessPageLocators():
    SUCCESS_MESSAGE = (By.XPATH, '//h1')
    CONTINUE_BUTTON = (By.XPATH, '//*[text() = "Continue"]')

class AccountPageLocators():
    EDIT_ACCOUNT = (By.XPATH, '//*[text() = "Edit your account information"]')

class ProfileLocators():
    NAME_LOCATOR = (By.XPATH, '//*[@id = "input-firstname"]')
    LASTNAME_LOCATOR = (By.XPATH, '//*[@id = "input-lastname"]')
    EMAIL_LOCATOR = (By.XPATH, '//*[@id = "input-email"]')
    PHONE_LOCATOR = (By.XPATH, '//*[@id = "input-telephone"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@type = "submit"]')