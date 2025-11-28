import time
from setup.base_test2 import BaseTest
<<<<<<< HEAD
from test_case.loginpage import LoginPage
=======
from page_objects.loginpom.loginpage import LoginPage
>>>>>>> a416327accb16a9584b6d982b9b88a6426acc2ef
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
<<<<<<< HEAD
        login.login(self.email, self.password)
        time.sleep(4)
=======

        login.login(self.email, self.password)
        time.sleep(4)


        # SELECT LOCATION
>>>>>>> a416327accb16a9584b6d982b9b88a6426acc2ef


        # SELECT LOCATION
        location.get_food_delivered()
        time.sleep(2)
        location.select_kathmandu()
        time.sleep(3)

        #  SEARCH PIZZA CUTTER RESTAURANT
<<<<<<< HEAD
        res.search_item("pizza")
        time.sleep(5)
        res.click_dropdown_pizza_cutter()
        time.sleep(3)
        res.click_card_pizza_cutter()
        time.sleep(3)
=======

        res.search_item("pizza")
        time.sleep(5)

        res.click_dropdown_pizza_cutter()
        time.sleep(3)

        res.click_card_pizza_cutter()
        time.sleep(3)

>>>>>>> a416327accb16a9584b6d982b9b88a6426acc2ef
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

<<<<<<< HEAD
        #Search next item cheese
=======
>>>>>>> a416327accb16a9584b6d982b9b88a6426acc2ef
        res.search_food_item("cheese")

        # Add cheese pizza
        cart.add_first_item()
        time.sleep(1)
        cart.open_cart()
        time.sleep(1)

        # Increase quantity
        cart.increase_quantity()
        time.sleep(1)
<<<<<<< HEAD
=======

>>>>>>> a416327accb16a9584b6d982b9b88a6426acc2ef
        res.search_food_item("chicken")
        time.sleep(2)

        # Add chicken pizza
        cart.add_first_item()
        time.sleep(1)
<<<<<<< HEAD
=======

>>>>>>> a416327accb16a9584b6d982b9b88a6426acc2ef
        cart.open_cart()
        time.sleep(1)

        # Increase chicken pizza by 2
        cart.increase_quantity()
        time.sleep(1)
        cart.increase_quantity()
        time.sleep(1)
<<<<<<< HEAD
        print("Pizza added to cart")


        #GO BACK to search again
        self.driver.back()
        time.sleep(2)

        #choose location
=======

        print("Pizza Cutter opened")
        #GO BACK to search again

        self.driver.back()
        time.sleep(2)

>>>>>>> a416327accb16a9584b6d982b9b88a6426acc2ef
        location.select_kathmandu()
        time.sleep(3)


        #  SEARCH SYANKO RESTAURANT
<<<<<<< HEAD
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
=======

        res.search_item("roll")
        time.sleep(5)

        res.click_dropdown_syanko()
        time.sleep(5)

        res.click_syanko_card()
        time.sleep(3)


        res.search_food_item("paneer")
        time.sleep(2)

        # Add cheese pizza
        cart.add_first_item()
        time.sleep(4)

        cart.click_yes_if_popup()

>>>>>>> a416327accb16a9584b6d982b9b88a6426acc2ef
        cart.open_cart()
        time.sleep(1)

        # Increase quantity
        cart.increase_quantity()
        time.sleep(1)
        print("Syanko Katti Roll opened")

        cart.increase_quantity()
        time.sleep(1)



