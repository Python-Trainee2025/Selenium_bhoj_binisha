from page_objects.cartpom.cartlocators import CartLocators

class CartProps(CartLocators):

    def __init__(self, driver):
        self.driver = driver


    def first_add_button(self):
        return self.driver.find_element(*CartLocators.ADD_BUTTON_FIRST)

    def cart_logo(self):
        return self.driver.find_element(*CartLocators.CART_LOGO)

    def increase_btn(self):
        return self.driver.find_element(*CartLocators.INCREASE_BTN)

    def decrease_btn(self):
        return self.driver.find_element(*CartLocators.DECREASE_BTN)

    def delete_btn(self):
        return self.driver.find_element(*CartLocators.DELETE_BTN)

    def checkout_btn(self):
        return self.driver.find_element(*CartLocators.CHECKOUT_BTN)

    def open_cart_btn(self):
        return self.driver.find_element(*CartLocators.OPEN_CART_BTN)

    def popup_yes_button(self):
        return self.driver.find_element(*self.YES_BTN)
