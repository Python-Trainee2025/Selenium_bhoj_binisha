from page_objects.change_passwordpom.change_props import ChangePasswordProps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.change_passwordpom.change_locator import ChangePasswordLocators
class ChangePasswordPage(ChangePasswordProps):

    def open_account(self):
        self.account_icon().click()

    def click_change_password(self):
        self.change_password_menu().click()

    def enter_old_password(self, value):
        self.old_password().clear()
        self.old_password().send_keys(value)

    def enter_new_password(self, value):
        self.new_password().clear()
        self.new_password().send_keys(value)

    def enter_confirm_password(self, value):
        self.confirm_password().clear()
        self.confirm_password().send_keys(value)

    def click_update(self):
        self.update_button().click()

    def change_password(self, old, new, confirm):
        self.enter_old_password(old)
        self.enter_new_password(new)
        self.enter_confirm_password(confirm)
        self.click_update()


    def wait_for_success(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(ChangePasswordLocators.SUCCESS_MSG)
        )

    def wait_for_error(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(ChangePasswordLocators.ERROR_MSG)
        )

    def wait_for_wrong_old(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(ChangePasswordLocators.WRONG_OLD_PASSWORD_MSG))


    def get_success_text(self):
        msg = self.success_message()
        return msg[0].text if msg else ""

    def get_error_text(self):
        msg = self.error_message()
        return msg[0].text if msg else ""

    def get_wrong_old_password_text(self):
        msg = self.wrong_old_message()
        return msg[0].text if msg else ""