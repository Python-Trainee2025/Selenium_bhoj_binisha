'''from page_objects.loginpom.loginlocator import LoginLocator

class LoginProperties(LoginLocator):

    @property
    def nav_login_btn(self):
        return self.driver.find_element(*self.LOGIN_BTN_NAV)

    @property
    def email(self):
        return self.driver.find_element(*self.EMAIL_INPUT)

    @property
    def password(self):
        return self.driver.find_element(*self.PASSWORD_INPUT)

    @property
    def submit_btn(self):
        return self.driver.find_element(*self.LOGIN_SUBMIT)

    @property
    def error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE)

    @property
    def login_before_checkout(self):
        return self.driver.find_element(*self.LOGIN_BEFORE_CHECKOUT)'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.loginpom.loginlocator import LoginLocator

class LoginProperties(LoginLocator):

    def wait_for(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @property
    def nav_login_btn(self):
        return self.wait_for(self.LOGIN_BTN_NAV)

    @property
    def email(self):
        return self.wait_for(self.EMAIL_INPUT)

    @property
    def password(self):
        return self.wait_for(self.PASSWORD_INPUT)

    @property
    def submit_btn(self):
        return self.wait_for(self.LOGIN_SUBMIT)

    @property
    def error_message(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )

    @property
    def login_before_checkout(self):
        return self.wait_for(self.LOGIN_BEFORE_CHECKOUT)
