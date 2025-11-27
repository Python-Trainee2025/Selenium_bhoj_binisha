import time
from selenium import webdriver
from page_objects.loginpom.loginpage import LoginPage
from page_objects.locationpom.location_page import LocationPage
from page_objects.search_restaurant_food.res_page import ResPage

from page_object import CartPage


class TestCart:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_cart_quantity(self):

        self.driver.get("https://www.bhojdeals.com/")
        time.sleep(2)

        login = LoginPage(self.driver)
        location= LocationPage(self.driver)
        search_res = ResPage(self.driver)

        cart = CartPage(self.driver)

        # Login
        login.login("loginproject03@gmail.com", "Project@123")

        location.get_food_delivered()
        time.sleep(2)

        location.select_kathmandu()
        time.sleep(2)

        search_res.search_item("pizza")
        time.sleep(2)
        search_res.click_dropdown_pizza_cutter()
        search_res.click_card_pizza_cutter()

        search_res.search_food_item("cheese")



        # Add cheese pizza
        cart.add_first_item()
        time.sleep(1)

        cart.open_cart()
        time.sleep(1)

        # Increase quantity
        cart.increase_quantity()
        time.sleep(1)

        # Decrease quantity
        cart.decrease_quantity()
        time.sleep(1)

        # Delete item
        cart.delete_item()
        time.sleep(1)


        # Search CHICKEN
        search_res.search_food_item("chicken")
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

        search_res.search_food_item("cheese")

        # Add cheese pizza
        cart.add_first_item()
        time.sleep(1)

        cart.open_cart()
        time.sleep(1)

        # Increase quantity
        cart.increase_quantity()
        time.sleep(1)
