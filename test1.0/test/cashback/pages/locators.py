from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD_LOCATOR = (By.XPATH, "//input[@id='LoginForm_username']")
    PASS_FIELD_LOCATOR = (By.XPATH, "//input[@id='LoginForm_password']")
    AUTH_BUTTON = (By.XPATH, "//button[@id='Authorization']")

class RegisterPageLocators:
    SPONSOR_YES_BUTTON = (By.XPATH, "//label/div[1]")
    SPONSOR_NOT_BUTTON = (By.XPATH, "//label/div[2]")
    SPONSOR_FIELD_LOCATOR = (By.XPATH, "//input[@id='ProfileRegister_sponsor__id']")
    USER_LOGIN_LOCATOR = (By.XPATH, "//input[@id='UsersRegister_username']")
    EMAIL_FIELD_LOCATOR = (By.XPATH, "//input[@id='UsersRegister_email']")
    SELECT_FIELD_LOCATOR = (By.XPATH, "//span[@id='select2-ProfileRegister_country__id-container']")
    PHONE_FIELD_LOCATOR = (By.XPATH, "//input[@id='ProfileRegister_phone']")
    PASS_FIELD_LOCATOR = (By.XPATH, "//input[@id = 'UsersRegister_password']")
    CHEKCBOX_LOCATOR = (By.XPATH, "//div//label/p[@class = 'span-bi']")
    REGISTER_BUTTON_LOCATOR = (By.XPATH, "//button[@id='registration']")

class MainPageLocators:
    REGISTER_LINK_LOCATOR = (By.XPATH, "//a[@class ='login__link _pad10'][2]")
    LOGIN_LINK_LOCATOR = (By.XPATH, "//a[@class ='login__link _pad10'][1]")

class OfficePageLocators:
    ALERT_MESSAGE_LOCATOR = (By.XPATH, "//div[@class='alert alert-danger']")
    ADMIN_PANEL_LINK_LOCATOR = (By.XPATH, "//a[text()='Админ-панель']")
    LOGOUT_LINK_LOCATOR = (By.XPATH, "//a[text()='Выход']")
    SUCCES_ALERT_LOCATOR = (By.XPATH, "//div[contains(@class,'alert-success')]/p")

class AdminPanelLocators:
    MAIL_PAGE_LINK_LOCATOR = (By.XPATH, "//a/span[text()='Письма']")
    OPEN_MAIL_LINK_LOCATOR = (By.XPATH, "//a[@class='btn blue-steel tooltips'][1]")
    CONFIRM_MAIL_LINK_LOCATOR = (By.LINK_TEXT, "Подтвердить")
    LOGOUT_ADMIN_LOCATOR = (By.XPATH, "")
