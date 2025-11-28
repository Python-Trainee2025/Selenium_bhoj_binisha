from selenium.webdriver.common.by import By

class LoginLocator:
    LOGIN_BTN_NAV = (By.XPATH, "//a[text()='login']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_SUBMIT = (By.XPATH, "//button[contains(text(),'Login')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-dismissible.alert-danger")
    LOGIN_BEFORE_CHECKOUT=(By.XPATH, "//a[contains(., 'Log In')]")
