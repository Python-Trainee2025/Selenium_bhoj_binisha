from page_objects.search_restaurant_food.res_locator import ResLocator

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
        return self.driver.find_element(*ResLocator.SYANKO_CARD)



