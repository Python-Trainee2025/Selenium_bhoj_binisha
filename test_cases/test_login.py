import time
from setup.base_test2 import BaseTest
from test_case.loginpage import LoginPage


class TestLogin(BaseTest):

    def test_valid_login(self):
        # Open the site using BaseTest method
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(3)

        login = LoginPage(self.driver)
<<<<<<< HEAD
=======

       
>>>>>>> a416327accb16a9584b6d982b9b88a6426acc2ef
        login.login(self.email, self.password)
