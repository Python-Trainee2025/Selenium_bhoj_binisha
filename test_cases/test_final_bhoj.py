import time
from setup.base_test2 import BaseTest
from page_objects.loginpom.login_page import LoginPage
from page_objects.locationpom.location_page import LocationPage
from page_objects.search_restaurant_food.res_page import ResPage
from page_objects.cartpom.cartpage import CartPage
from page_objects.checkout.checkoutpage import CheckoutPage
from page_objects.change_passwordpom.change_page import ChangePasswordPage
from page_objects.logoutpom.logout_page import LogoutPage


class TestCheckout(BaseTest):

    def test_checkout_flow(self):
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(2)

        login = LoginPage(self.driver)
        location = LocationPage(self.driver)
        search_res = ResPage(self.driver)
        cart = CartPage(self.driver)
        checkout = CheckoutPage(self.driver)
        profile = ChangePasswordPage(self.driver)
        logout = LogoutPage(self.driver)

        #search without login
        location.get_food_delivered()
        time.sleep(1)
        location.select_kathmandu()

        search_res.search_item("pizza")
        time.sleep(3)
        search_res.click_dropdown_pizza_cutter()
        time.sleep(3.5)
        search_res.click_card_pizza_cutter()
        time.sleep(3.5)


        # chicken PIZZA
        search_res.search_food_item("chicken")
        time.sleep(3.5)
        cart.add_first_item()
        time.sleep(3.5)
        cart.open_cart()
        time.sleep(3.5)
        cart.increase_quantity()
        time.sleep(3.5)
        cart.decrease_quantity()
        time.sleep(3.5)


        # search for next item cheese pizza
        search_res.search_food_item("cheese")
        time.sleep(3.5)
        cart.add_first_item()
        time.sleep(3.5)
        cart.open_cart()
        time.sleep(3.5)
        cart.increase_quantity()
        time.sleep(3.5)
        cart.delete_item()
        time.sleep(3.5)
        cart.add_first_item()
        time.sleep(3.5)
        cart.open_cart()
        time.sleep(3.5)


        # go back to search again
        self.driver.back()
        time.sleep(2)
        location.select_kathmandu()
        time.sleep(2)

        #  search syanko restaurant
        search_res.search_item("roll")
        time.sleep(3)
        search_res.click_dropdown_syanko()
        time.sleep(3)
        search_res.click_syanko_card()
        time.sleep(3.5)
        search_res.search_food_item("paneer")
        time.sleep(3.5)

        # Add paneer roll
        cart.add_first_item()
        time.sleep(3)
        cart.click_yes_if_popup()
        cart.open_cart()
        time.sleep(3.5)
        cart.increase_quantity()
        time.sleep(3.5)

        # go to checkout

        checkout.click_proceed_checkout()
        time.sleep(1)

        login.login_before()
        time.sleep(2)

        login.login(self.email, self.password)
        time.sleep(2)


        # complete checkout

        checkout.increase_quantity(times=2)
        time.sleep(1)
        checkout.decrease_quantity(times=1)
        time.sleep(2)

        subtotal = checkout.subtotal.text
        total = checkout.total_amount.text

        print("Subtotal:", subtotal)
        print("Total:", total)

        assert "Rs" in subtotal
        assert "Rs" in total

        checkout.select_cod()
        time.sleep(2)

        #change password
        profile.open_account()
        time.sleep(3)
        profile.click_change_password()

        print("\n STEP 1: Wrong old password ")
        profile.change_password("WrongPass@123", "NewPass@123", "NewPass@123")
        time.sleep(1)

        assert "valid old password" in profile.get_wrong_old_password_text()
        print(" Error displayed: Wrong old password")

        print("\n STEP 2: Password mismatch ")
        profile.change_password(self.password, "NewPass@123", "Mismatch@123")
        time.sleep(1)

        assert "match" in profile.get_error_text()
        print(" Error displayed: Password mismatch")

        print("\n STEP 3: Weak password ")
        profile.change_password(self.password, "weak", "weak")
        time.sleep(1)

        assert "8" in profile.get_error_text() or "character" in profile.get_error_text()
        print("Error displayed: Weak password")

        print("\n STEP 4: Correct password (Success) ")
        new_pass = "Project@123"

        profile.change_password(self.password, new_pass, new_pass)
        time.sleep(2)

        msg = profile.get_success_text()
        print(f"Success message shown: {msg}")
        print("Password changed successfully!")

        # logout

        logout.click_logout()
        time.sleep(1)
        logout.confirm_logout()
        time.sleep(1)
