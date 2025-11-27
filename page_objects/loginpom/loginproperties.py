from page_objects.loginpom.loginlocator import LoginLocator

class LoginProperties:

    @property
    def nav_login_btn(self):
        return self.driver.find_element(*LoginLocator.LOGIN_BTN_NAV)

    @property
    def email(self):
        return self.driver.find_element(*LoginLocator.EMAIL_INPUT)

    @property
    def password(self):
        return self.driver.find_element(*LoginLocator.PASSWORD_INPUT)

    @property
    def submit_btn(self):
        return self.driver.find_element(*LoginLocator.LOGIN_SUBMIT)

    @property
    def error_message(self):
        return self.driver.find_element(*LoginLocator.ERROR_MESSAGE)
