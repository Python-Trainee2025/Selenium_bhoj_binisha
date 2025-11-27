import time
from setup.base_test2 import BaseTest
from page_objects.change_passwordpom.change_page import ChangePasswordPage
from page_objects.loginpom.loginpage import LoginPage

class TestChangePassword(BaseTest):

    def test_change_password(self):
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(2)

        profile = ChangePasswordPage(self.driver)
        login = LoginPage(self.driver)

        # LOGIN
        login.login(self.email, self.password)
        time.sleep(2)

        profile.open_account()
        profile.click_change_password()
        time.sleep(1)

        print("\n STEP 1: Wrong old password ")
        profile.change_password("WrongPass@123", "NewPass@123", "NewPass@123")
        time.sleep(1)

        assert "valid old password" in profile.get_wrong_old_password_text()
        print(" Error displayed: Wrong old password")

        print("\n STEP 2: Password mismatch ")
        profile.change_password(self.password, "NewPass@123", "Mismatch@123")
        time.sleep(1)

        assert "match" in profile.get_error_text()
        print(" Error displayed: Password mismatch")

        print("\n STEP 3: Weak password ")
        profile.change_password(self.password, "weak", "weak")
        time.sleep(1)

        assert "8" in profile.get_error_text() or "character" in profile.get_error_text()
        print("Error displayed: Weak password")

        print("\n STEP 4: Correct password (Success) ")
        new_pass = "Bhoj@123"

        profile.change_password(self.password, new_pass, new_pass)
        time.sleep(2)

        msg = profile.get_success_text()
        print(f"Success message shown: {msg}")  
        print("Password changed successfully!")
