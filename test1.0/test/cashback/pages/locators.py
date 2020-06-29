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
