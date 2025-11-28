from selenium.webdriver.common.by import By

class CartLocators:
    ADD_BUTTON_FIRST = (By.XPATH, "(//a[normalize-space()='ADD'])[1]")
     # Cart logo count (top right number)
    CART_LOGO = (By.CSS_SELECTOR, "span[data-v-63cbf0a8]")

    # Increase quantity (+)
    INCREASE_BTN = (By.CSS_SELECTOR, "i.icon-add")

    # Decrease quantity (-)
    DECREASE_BTN = (By.CSS_SELECTOR, "i.icon-remove")

    # Delete item link
    DELETE_BTN = (By.CSS_SELECTOR, "a.delete-note")

    # Checkout button
    CHECKOUT_BTN = (By.CSS_SELECTOR, "button[data-v-63cbf0a8]")

    # Cart icon/button to open cart panel
    OPEN_CART_BTN = (By.CSS_SELECTOR, "div.cart-icon, span[data-v-63cbf0a8]")


    YES_BTN = (By.XPATH, "//button[normalize-space()='YES']")