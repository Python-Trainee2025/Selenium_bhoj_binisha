import time
from page_objects.checkout.checkoutprops import CheckoutProperties


class CheckoutPage(CheckoutProperties):

    def __init__(self, driver):
        super().__init__(driver)

    # BUTTONS
    def click_proceed_checkout(self):
        self.proceed_checkout_btn.click()

    def click_confirm_order(self):
        self.confirm_order_btn.click()

    # QUANTITY
    def increase_quantity(self, times=1):
        for _ in range(times):
            self.qty_increase.click()
            time.sleep(0.3)

    def decrease_quantity(self, times=1):
        for _ in range(times):
            self.qty_decrease.click()
            time.sleep(0.3)

    # DELIVERY OPTIONS
    def select_call_yes(self):
        self.call_yes.click()

    def select_leave_food_no(self):
        self.leave_food_no.click()

    def select_cod(self):
        self.cod_payment.click()


    def click_confirm(self):
        self.confirm_order_btn.click()
