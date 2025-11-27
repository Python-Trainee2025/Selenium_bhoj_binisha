import time
from page_objects.search_restaurant_food.res_props import ResProps



class ResPage(ResProps):
    def __init__(self, driver):
        self.driver = driver

    def search_item(self, item):
        self.search_bar.send_keys(item)
        time.sleep(3)


    def click_dropdown_pizza_cutter(self):
        time.sleep(2)
        self.dropdown_pizza_cutter.click()
        time.sleep(3)

    def click_card_pizza_cutter(self):
        time.sleep(2)
        self.card_pizza_cutter.click()
        time.sleep(3)

    def search_food_item(self, item):
        time.sleep(1)
        self.menu_search_bar.clear()
        self.menu_search_bar.send_keys(item)
        time.sleep(2)

    def click_dropdown_syanko(self):
        self.dropdown_syanko.click()
        time.sleep(2)

    def click_syanko_card(self):
        self.syanko_card.click()
        time.sleep(3)


