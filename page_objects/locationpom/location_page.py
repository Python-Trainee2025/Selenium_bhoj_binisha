import time
from page_objects.locationpom.location_props import LocationProps

class LocationPage(LocationProps):

    def get_food_delivered(self):
        self.get_food_btn().click()

    def select_kathmandu(self):
        self.get_kathmandu_btn().click()

    def select_bhaktapur(self):
        self.get_bhaktapur_btn().click()