import time
from page_objects.loginpom.loginproperties import LoginProperties

class LoginPage(LoginProperties):

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        time.sleep(3)
        self.nav_login_btn.click()
        time.sleep(2)

        self.email.send_keys(email)
        time.sleep(1)

        self.password.send_keys(password)
        time.sleep(1)

        self.submit_btn.click()
        time.sleep(5)


    def get_error_message(self):
        """Returns login error message if exists."""
        try:
            return self.error_message.text.strip()
        except NoSuchElementException:
            return None
