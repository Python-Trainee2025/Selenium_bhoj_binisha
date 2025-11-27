import time
from setup.base_test2 import BaseTest
from page_objects.loginpom.loginpage import LoginPage

class TestLogin(BaseTest):

    def test_invalid_login(self):
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(2)

        login = LoginPage(self.driver)

        login.login("wrong@mail.com", "wrongPass123")

        error = login.get_error_message()

        assert error is not None
        print("Error:", error)
