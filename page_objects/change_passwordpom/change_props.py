'''from page_objects.change_passwordpom.change_locator import ChangePasswordLocators

class ChangePasswordProps:

    def __init__(self, driver):
        self.driver = driver

    def account_icon(self):
        return self.driver.find_element(*ChangePasswordLocators.ACCOUNT_ICON)

    def change_password_menu(self):
        return self.driver.find_element(*ChangePasswordLocators.CHANGE_PASSWORD_MENU)

    def old_password(self):
        return self.driver.find_element(*ChangePasswordLocators.OLD_PASSWORD)

    def new_password(self):
        return self.driver.find_element(*ChangePasswordLocators.NEW_PASSWORD)

    def confirm_password(self):
        return self.driver.find_element(*ChangePasswordLocators.CONFIRM_PASSWORD)

    def update_button(self):
        return self.driver.find_element(*ChangePasswordLocators.UPDATE_BUTTON)

    def success_message(self):
        return self.driver.find_elements(*ChangePasswordLocators.SUCCESS_MSG)

    def error_message(self):
        return self.driver.find_elements(*ChangePasswordLocators.ERROR_MSG)

    def wrong_old_message(self):
        return self.driver.find_elements(*ChangePasswordLocators.WRONG_OLD_PASSWORD_MSG)'''

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.change_passwordpom.change_locator import ChangePasswordLocators

class ChangePasswordProps:

    def __init__(self, driver):
        self.driver = driver

    def wait_for(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_all(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def account_icon(self):
        return self.wait_for(ChangePasswordLocators.ACCOUNT_ICON)

    def change_password_menu(self):
        return self.wait_for(ChangePasswordLocators.CHANGE_PASSWORD_MENU)

    def old_password(self):
        return self.wait_for(ChangePasswordLocators.OLD_PASSWORD)

    def new_password(self):
        return self.wait_for(ChangePasswordLocators.NEW_PASSWORD)

    def confirm_password(self):
        return self.wait_for(ChangePasswordLocators.CONFIRM_PASSWORD)

    def update_button(self):
        return self.wait_for(ChangePasswordLocators.UPDATE_BUTTON)

    def success_message(self):
        return self.wait_for_all(ChangePasswordLocators.SUCCESS_MSG)

    def error_message(self):
        return self.wait_for_all(ChangePasswordLocators.ERROR_MSG)

    def wrong_old_message(self):
        return self.wait_for_all(ChangePasswordLocators.WRONG_OLD_PASSWORD_MSG)

