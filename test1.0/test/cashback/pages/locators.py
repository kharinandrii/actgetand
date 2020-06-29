from selenium.webdriver.common.by import By

class MainPageLocators():
    MY_ACCOUNT_DROBDOWN =  (By.XPATH, '//*[@class = "list-inline"]//*[text()="My Account"]')
    REGISTER_LINK = (By.XPATH, '//*[text()="Register"]')

class SavePageLocators():
    DETAIL_BUTTON = (By.XPATH, '//*[@id = "details-button"]')
    PROCESS_LINK = (By.XPATH, '//*[@id = "proceed-link"]')

class RegisterPageLocators():
    FIRST_NAME = (By.XPATH, '//*[@id = "input-firstname"]')