import time
from page_objects.loginpom.loginproperties import LoginProperties
from selenium.common.exceptions import NoSuchElementException

class LoginPage(LoginProperties):

    def __init__(self, driver):
        self.driver = driver

    def open_login(self):
        self.nav_login_btn.click()
        time.sleep(2)

    def login(self, email, password):

        self.email.send_keys(email)
        time.sleep(1)

        self.password.send_keys(password)
        time.sleep(1)

        self.submit_btn.click()
        time.sleep(5)

    def login_before(self):
        self.login_before_checkout.click()

    def get_error_message(self):
        """Returns login error message if exists."""
        try:
            return self.error_message.text.strip()
        except NoSuchElementException:
            return None

    def clear_fields(self):
        """Locate fresh elements and clear fields properly."""
        try:
            email_input = self.driver.find_element(*self.EMAIL_INPUT)
            password_input = self.driver.find_element(*self.PASSWORD_INPUT)

            email_input.clear()
            password_input.clear()
        except Exception as e:
            print("Could not clear fields:", e)


