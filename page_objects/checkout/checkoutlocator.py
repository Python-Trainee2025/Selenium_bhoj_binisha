from selenium.webdriver.common.by import By


class CheckoutLocators:
    PROCEED_CHECKOUT = (By.CSS_SELECTOR, "button.btn.btn-secondary")
    INCREASE_QTY = (By.CSS_SELECTOR, "i.icon-add")
    DECREASE_QTY = (By.CSS_SELECTOR, "i.icon-remove")

    SUBTOTAL = (By.XPATH, "//h4[contains(text(),'Restaurant Subtotal')]/../following-sibling::div/p")
    DELIVERY_CHARGE = (By.XPATH, "//h4[contains(text(),'Delivery Charge')]/../following-sibling::div/p")
    TOTAL_AMOUNT = (By.XPATH, "//h4[contains(text(),'Restaurant Total')]/../following-sibling::div/p")

    CALL_YES = (By.CSS_SELECTOR, "label.custom-control-label[for='call-yes']")
    LEAVE_FOOD_NO = (By.CSS_SELECTOR, "label.custom-control-label[for='no']")


    CASH_ON_DELIVERY = (By.CSS_SELECTOR, "label[for='radiobtn']")
    CONFIRM_ORDER_BTN = (By.CLASS,"btn btn-secondary")
