import time
from setup.base_test2 import BaseTest
from test_case.loginpage import LoginPage
from page_objects.locationpom.location_page import LocationPage
from page_objects.search_restaurant_food.res_page import ResPage


class TestRestaurantSearch(BaseTest):

    def test_login_and_search_restaurants(self):
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(3)

        login = LoginPage(self.driver)
        location = LocationPage(self.driver)
        restaurant = ResPage(self.driver)

        # LOGIN FIRST

        login.login(self.email, self.password)
        time.sleep(4)

        # SELECT LOCATION

        location.get_food_delivered()
        time.sleep(2)
        location.select_kathmandu()
        time.sleep(3)

        #  SEARCH PIZZA CUTTER RESTAURANT

        restaurant.search_item("pizza")
        time.sleep(5)
        restaurant.click_dropdown_pizza_cutter()
        time.sleep(3)
        restaurant.click_card_pizza_cutter()
        time.sleep(3)
        restaurant.search_food_item("cheese")
        time.sleep(2)
        print("Pizza Cutter opened")

        # GO BACK to search again

        self.driver.back()
        time.sleep(2)
        location.select_kathmandu()
        time.sleep(3)

        #  SEARCH SYANKO RESTAURANT

        restaurant.search_item("roll")
        time.sleep(5)
        restaurant.click_dropdown_syanko()
        time.sleep(5)
        restaurant.click_syanko_card()
        time.sleep(3)
        restaurant.search_food_item("chicken")
        time.sleep(2)
        print("Syanko Katti Roll opened")
