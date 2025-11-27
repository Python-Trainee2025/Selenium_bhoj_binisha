from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.logoutpom.logout_locator import LogoutLocators


class LogoutPage:

    BACKDROP = (By.CSS_SELECTOR, "div.loading-backdrop")

    def __init__(self, driver):
        self.driver = driver

    def wait_for_backdrop(self):
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located(self.BACKDROP)
        )

    def open_account(self):
        self.wait_for_backdrop()
        self.driver.find_element(*LogoutLocators.ACCOUNT_ICON).click()

    def click_logout(self):
        self.wait_for_backdrop()
        self.driver.find_element(*LogoutLocators.LOGOUT_BUTTON).click()

    def confirm_logout(self):
        self.wait_for_backdrop()
        self.driver.find_element(*LogoutLocators.LOGOUT_CONFIRM_YES).click()
