import time
from selenium import webdriver
from page_objects.loginpom.loginpage import LoginPage
from page_objects.logoutpom.logout_page import LogoutPage

class TestLogout:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_logout(self):
        self.driver.get("https://www.bhojdeals.com/")
        time.sleep(4)

        login = LoginPage(self.driver)
        logout = LogoutPage(self.driver)

        # Login first
        login.login("binisha077bei010@gmail.com", "Bhoj@123")
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

        # Optional assert
        # assert "Login" in self.driver.page_source
