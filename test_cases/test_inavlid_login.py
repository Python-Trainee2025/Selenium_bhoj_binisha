import time
import logging
from setup.base_test2 import BaseTest
from page_objects.loginpom.login_page import LoginPage

class TestLogin(BaseTest):
    def test_invalid_login(self):
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(2)
        login = LoginPage(self.driver)
        login.open_login()
        login.login("wrong@mail.com", "wrongPass123")

        error = login.get_error_message()

        assert error is not None
        logging.info(f"Error: {error}")
