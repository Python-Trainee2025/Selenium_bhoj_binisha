from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.checkout.checkoutlocator import CheckoutLocators


class CheckoutProperties(CheckoutLocators):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # QUANTITY
    @property
    def qty_increase(self):
        return self.wait.until(EC.element_to_be_clickable(CheckoutLocators.INCREASE_QTY))

    @property
    def qty_decrease(self):
        return self.wait.until(EC.element_to_be_clickable(CheckoutLocators.DECREASE_QTY))

    # PRICE
    @property
    def subtotal(self):
        return self.wait.until(EC.visibility_of_element_located(CheckoutLocators.SUBTOTAL))

    @property
    def delivery_charge(self):
        return self.wait.until(EC.visibility_of_element_located(CheckoutLocators.DELIVERY_CHARGE))

    @property
    def total_amount(self):
        return self.wait.until(EC.visibility_of_element_located(CheckoutLocators.TOTAL_AMOUNT))

    # DELIVERY OPTIONS
    @property
    def call_yes(self):
        return self.wait.until(EC.element_to_be_clickable(CheckoutLocators.CALL_YES))

    @property
    def leave_food_no(self):
        return self.wait.until(EC.element_to_be_clickable(CheckoutLocators.LEAVE_FOOD_NO))

    # PAYMENT
    @property
    def cod_payment(self):
        return self.wait.until(EC.element_to_be_clickable(CheckoutLocators.CASH_ON_DELIVERY))

    # BUTTONS
    @property
    def proceed_checkout_btn(self):
        return self.wait.until(EC.element_to_be_clickable(CheckoutLocators.PROCEED_CHECKOUT))

    @property
    def confirm_order_btn(self):
        return self.wait.until(EC.element_to_be_clickable(CheckoutLocators.CONFIRM_ORDER_BTN))
