from page_objects.cartpom.cartprops import CartProps
from selenium.common.exceptions import NoSuchElementException
import time

class CartPage(CartProps):


    def add_first_item(self):
        time.sleep(1)
        self.first_add_button().click()
        time.sleep(2)

    def open_cart(self):
        self.open_cart_btn().click()
        time.sleep(1)

    def get_cart_count(self):
        return int(self.cart_logo().text.strip())

    def increase_quantity(self):
        self.increase_btn().click()

    def decrease_quantity(self):
        self.decrease_btn().click()

    def delete_item(self):
        self.delete_btn().click()

    def click_checkout(self):
        self.checkout_btn().click()


    def click_yes_if_popup(self):
        """Always click YES if popup appears (no condition)."""
        try:
            self.popup_yes_button().click()
            time.sleep(1)
        except NoSuchElementException:
            pass


