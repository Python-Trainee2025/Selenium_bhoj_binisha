from page_objects.loginpom.loginlocator import LoginLocator

class LoginProperties(LoginLocator):

    @property
    def nav_login_btn(self):
        return self.driver.find_element(*self.LOGIN_BTN_NAV)

    @property
    def email(self):
        return self.driver.find_element(*self.EMAIL_INPUT)

    @property
    def password(self):
        return self.driver.find_element(*self.PASSWORD_INPUT)

    @property
    def submit_btn(self):
        return self.driver.find_element(*self.LOGIN_SUBMIT)

    @property
    def error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE)

    @property
    def login_before_checkout(self):
        return self.driver.find_element(*self.LOGIN_BEFORE_CHECKOUT)
