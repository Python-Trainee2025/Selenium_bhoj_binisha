import time
from setup.base_test2 import BaseTest
from page_objects.locationpom.location_page import LocationPage

from test_case.loginpage import LoginPage


class TestLocation(BaseTest):

    def test_location_selection(self):

        self.open_url("https://www.bhojdeals.com/")
        time.sleep(2)

        login = LoginPage(self.driver)
        location = LocationPage(self.driver)


        # LOGIN
        login.login(self.email, self.password)
        time.sleep(2)

        location.get_food_delivered()
        time.sleep(2)

        location.select_kathmandu()
        time.sleep(2)
