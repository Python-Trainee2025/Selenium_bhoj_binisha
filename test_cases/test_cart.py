import time
import logging
from setup.base_test2 import BaseTest
from page_objects.loginpom.login_page import LoginPage
from page_objects.locationpom.location_page import LocationPage
from page_objects.search_restaurant_food.res_page import ResPage
from page_objects.cartpom.cartpage import CartPage


class TestRestaurantSearch(BaseTest):

    def test_login_and_search_restaurants(self):


        self.open_url("https://www.bhojdeals.com/")
        time.sleep(3)

        login = LoginPage(self.driver)
        location = LocationPage(self.driver)
        res = ResPage(self.driver)
        cart=CartPage(self.driver)


        # LOGIN FIRST
        login.open_login()
        login.login(self.email, self.password)
        time.sleep(4)


        # SELECT LOCATION
        location.get_food_delivered()
        time.sleep(2)
        location.select_kathmandu()
        time.sleep(3)

        #  SEARCH PIZZA CUTTER RESTAURANT
        res.search_item("pizza")
        time.sleep(5)
        res.click_dropdown_pizza_cutter()
        time.sleep(3)
        res.click_card_pizza_cutter()
        time.sleep(3)
        res.search_food_item("chicken")
        time.sleep(2)

        # Add chicken pizza
        cart.add_first_item()
        time.sleep(1)
        cart.open_cart()
        time.sleep(1)

        # Increase chicken pizza by 2
        cart.increase_quantity()
        time.sleep(1)
        cart.increase_quantity()
        time.sleep(1)

        # Delete item
        cart.delete_item()
        time.sleep(1)

        #Search next item cheese
        res.search_food_item("cheese")

        # Add cheese pizza
        cart.add_first_item()
        time.sleep(1)
        cart.open_cart()
        time.sleep(1)

        # Increase quantity
        cart.increase_quantity()
        time.sleep(1)
        res.search_food_item("chicken")
        time.sleep(2)

        # Add chicken pizza
        cart.add_first_item()
        time.sleep(1)
        cart.open_cart()
        time.sleep(1)

        # Increase chicken pizza by 2
        cart.increase_quantity()
        time.sleep(1)
        cart.increase_quantity()
        time.sleep(1)
        logging.info("Pizza added to cart")


        #GO BACK to search again
        self.driver.back()
        time.sleep(2)

        #choose location
        location.select_kathmandu()
        time.sleep(3)


        #  SEARCH SYANKO RESTAURANT
        res.search_item("roll")
        time.sleep(5)
        res.click_dropdown_syanko()
        time.sleep(5)
        res.click_syanko_card()
        time.sleep(3)
        res.search_food_item("paneer")
        time.sleep(2)

        # Add paneer roll
        cart.add_first_item()
        time.sleep(4)
        cart.click_yes_if_popup()
        cart.open_cart()
        time.sleep(1)

        # Increase quantity
        cart.increase_quantity()
        time.sleep(1)
        logging.info("Syanko Katti Roll opened")

        cart.increase_quantity()
        time.sleep(1)



