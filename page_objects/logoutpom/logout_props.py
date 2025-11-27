from page_objects.logoutpom.logout_locator import LogoutLocators

class LogoutProps:

    def __init__(self, driver):
        self.driver = driver

    def account_icon(self):
        return self.driver.find_element(*LogoutLocators.ACCOUNT_ICON)

    def logout_button(self):
        return self.driver.find_element(*LogoutLocators.LOGOUT_BUTTON)

    def logout_confirm_yes(self):
        return self.driver.find_element(*LogoutLocators.LOGOUT_CONFIRM_YES)
