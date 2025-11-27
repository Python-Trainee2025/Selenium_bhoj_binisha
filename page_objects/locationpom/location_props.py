from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from page_objects.locationpom.location_locator import LocationLocators

class LocationProps(LocationLocators):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def get_food_btn(self):
        return self.wait.until(
            EC.element_to_be_clickable(LocationLocators.GET_FOOD_BTN )
        )

    def get_kathmandu_btn(self):
        return self.wait.until(
            EC.element_to_be_clickable(LocationLocators.LOCATION_KTM)
        )

    def get_bhaktapur_btn(self):
        return self.wait.until(
            EC.element_to_be_clickable(LocationLocators.LOCATION_BKT)
        )


