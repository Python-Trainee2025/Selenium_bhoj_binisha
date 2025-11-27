from selenium.webdriver.common.by import By


class ChangePasswordLocators:
    ACCOUNT_ICON = (By.CSS_SELECTOR, "img.account-img")
    CHANGE_PASSWORD_MENU = (By.CSS_SELECTOR, 'a[href="/changepassword"]')
    OLD_PASSWORD = (By.XPATH, '(//input[@type="password"])[1]')
    NEW_PASSWORD = (By.XPATH, '(//input[@type="password"])[2]')
    CONFIRM_PASSWORD = (By.XPATH, '(//input[@type="password"])[3]')
    UPDATE_BUTTON = (By.XPATH, '//button[@type="submit"]')

    # Messages
    SUCCESS_MSG = (By.CSS_SELECTOR, ".alert-success")


    ERROR_MSG = (By.CSS_SELECTOR, ".invalid-message")   # weak password, mismatch
    WRONG_OLD_PASSWORD_MSG = (By.CSS_SELECTOR, ".alert-danger")