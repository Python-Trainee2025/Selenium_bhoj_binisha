from selenium.webdriver.common.by import By

class LogoutLocators:
    ACCOUNT_ICON = (By.CSS_SELECTOR, "img.account-img")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(., 'Logout')]")
    LOGOUT_CONFIRM_YES = (By.CSS_SELECTOR, "button.btn.btn-outline-primary")
