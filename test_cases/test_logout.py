import time
from setup.base_test2 import BaseTest
from page_objects.loginpom.login_page import LoginPage
from page_objects.logoutpom.logout_page import LogoutPage

class TestLogout(BaseTest):

    def test_logout(self):
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(4)


        login = LoginPage(self.driver)
        logout = LogoutPage(self.driver)

        # Login first
        login.open_login()
        login.login(self.email, self.password)
        time.sleep(2)

        # Open account dropdown
        logout.open_account()
        time.sleep(1)

        # Click logout
        logout.click_logout()
        time.sleep(1)

        # Confirm logout
        logout.confirm_logout()
        time.sleep(1)


