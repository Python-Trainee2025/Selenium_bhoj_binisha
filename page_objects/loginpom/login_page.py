import time

from selenium.common.exceptions import NoSuchElementException
from page_objects.loginpom.loginlocator import LoginLocator
from page_objects.loginpom.loginproperties import LoginProperties

class LoginPage(LoginProperties):

    def __init__(self, driver):
        self.driver = driver

    def clear_fields(self):
        try:
            self.email.clear()
            self.password.clear()
        except:
            pass

    def login_before(self):
        self.login_before_checkout.click()

    def login(self, email, password):
        self.email.send_keys(email)
        self.password.send_keys(password)
        self. submit_btn.click()
        time.sleep(1)

        if self.is_error_displayed():
            self.clear_fields()

    def get_error_message(self):
        try:
            return self.driver.find_element(*self. error_message).text
        except NoSuchElementException:
            return None

    def is_error_displayed(self):
        return self.get_error_message() is not None
