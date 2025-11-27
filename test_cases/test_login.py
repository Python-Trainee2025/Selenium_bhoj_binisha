import time
from setup.base_test2 import BaseTest
from page_objects.loginpom.loginpage import LoginPage


class TestLogin(BaseTest):

    def test_valid_login(self):
        # Open the site using BaseTest method
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(3)

        login = LoginPage(self.driver)

       
        login.login(self.email, self.password)
