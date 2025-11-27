from selenium.webdriver.common.by import By

class LocationLocators:
    GET_FOOD_BTN = (By.XPATH,"//a[.//h2[contains(text(),'Get Food')]]")
    # Kathmandu card
    LOCATION_KTM = (By.CSS_SELECTOR, "img[title='Kathmandu and Lalitpur']")
    LOCATION_BKT = (
    By.XPATH,
    "//h2[contains(text(),'Bhaktapur')]"
)


