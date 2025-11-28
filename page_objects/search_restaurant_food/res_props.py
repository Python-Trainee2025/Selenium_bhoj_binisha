'''from page_objects.search_restaurant_food.res_locator import ResLocator

class ResProps(ResLocator):

    @property
    def search_bar(self):
        return self.driver.find_element(*ResLocator.SEARCH_BAR)


    @property
    def dropdown_pizza_cutter(self):
        return self.driver.find_element(*ResLocator.DROPDOWN_PIZZA_CUTTER)

    @property
    def card_pizza_cutter(self):
        return self.driver.find_element(*ResLocator.CARD_PIZZA_CUTTER)

    @property
    def menu_search_bar(self):
        return self.driver.find_element(*ResLocator.MENU_SEARCH_BAR)

    @property
    def dropdown_syanko(self):
        return self.driver.find_element(*ResLocator.DROPDOWN_SYANKO)

    @property
    def syanko_card(self):
        return self.driver.find_element(*ResLocator.SYANKO_CARD)'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.search_restaurant_food.res_locator import ResLocator

class ResProps(ResLocator):

    def wait_for(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @property
    def search_bar(self):
        return self.wait_for(self.SEARCH_BAR)

    @property
    def dropdown_pizza_cutter(self):
        return self.wait_for(self.DROPDOWN_PIZZA_CUTTER)

    @property
    def card_pizza_cutter(self):
        return self.wait_for(self.CARD_PIZZA_CUTTER)

    @property
    def menu_search_bar(self):
        return self.wait_for(self.MENU_SEARCH_BAR)

    @property
    def dropdown_syanko(self):
        return self.wait_for(self.DROPDOWN_SYANKO)

    @property
    def syanko_card(self):
        return self.wait_for(self.SYANKO_CARD)




