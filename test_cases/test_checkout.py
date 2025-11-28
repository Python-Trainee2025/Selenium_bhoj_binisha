import time
from setup.base_test2 import BaseTest
from test_case.loginpage import LoginPage
from page_objects.locationpom.location_page import LocationPage
from page_objects.search_restaurant_food.res_page import ResPage
from page_objects.cartpom.cartpage import CartPage
from page_objects.checkout.checkoutpage import CheckoutPage


class TestCheckout(BaseTest):

    def test_checkout_flow(self):
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(2)


        login = LoginPage(self.driver)
        location = LocationPage(self.driver)
        search_res= ResPage(self.driver)
        cart = CartPage(self.driver)
        checkout = CheckoutPage(self.driver)



        login.login(self.email, self.password)
        time.sleep(3)


        # LOCATION SELECTION

        location.get_food_delivered()
        time.sleep(2)
        location.select_kathmandu()
        time.sleep(2)


        # SEARCH RESTAURANT
        search_res.search_item("pizza")
        time.sleep(2)
        search_res.click_dropdown_pizza_cutter()
        time.sleep(2)
        search_res.click_card_pizza_cutter()
        time.sleep(2)


        # FIRST: chicken PIZZA FLOW
        search_res.search_food_item("chicken")
        cart.add_first_item()
        time.sleep(1)
        cart.open_cart()
        time.sleep(1)
        cart.increase_quantity()
        time.sleep(1)
        cart.decrease_quantity()
        time.sleep(1)


        # search for next item cheese pizza
        search_res.search_food_item("cheese")
        time.sleep(1)
        cart.add_first_item()
        time.sleep(1)
        cart.open_cart()
        time.sleep(1)
        cart.increase_quantity()
        time.sleep(1)
        cart.delete_item()
        time.sleep(1)
        cart.add_first_item()
        time.sleep(1)
        cart.open_cart()
        time.sleep(1)


        # GO BACK to search again
        self.driver.back()
        time.sleep(2)
        location.select_kathmandu()
        time.sleep(3)

        #  SEARCH SYANKO RESTAURANT
        search_res.search_item("roll")
        time.sleep(5)
        search_res.click_dropdown_syanko()
        time.sleep(5)
        search_res.click_syanko_card()
        time.sleep(3)
        search_res.search_food_item("paneer")
        time.sleep(2)
        print("Syanko Katti Roll has been added")

        # CHECKOUT PROCESS
        checkout.click_proceed_checkout()
        time.sleep(2)
        checkout.increase_quantity(times=2)
        time.sleep(1)
        checkout.decrease_quantity(times=1)
        time.sleep(1)

        # PRICE ASSERTION
        subtotal = checkout.subtotal.text
        delivery = checkout.delivery_charge.text
        total = checkout.total_amount.text

        print("Subtotal:", subtotal)
        print("Delivery:", delivery)
        print("Total:", total)

        assert "Rs" in subtotal
        assert "Rs" in delivery
        assert "Rs" in total

        # DELIVERY OPTIONS
        checkout.select_call_yes()
        time.sleep(2)
        checkout.select_leave_food_no()
        time.sleep(2)
        # PAYMENT METHOD
        checkout.select_cod()
        time.sleep(3)

        assert True
