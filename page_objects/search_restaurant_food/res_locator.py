from selenium.webdriver.common.by import By

class ResLocator:
    SEARCH_BAR = (By.CSS_SELECTOR, "input[placeholder='Search']")

    DROPDOWN_PIZZA_CUTTER = (By.XPATH, "//*[@id='mybhojapp']/div[2]/section/div/div/div[2]/div/div/div/ul/li[4]/div")

    CARD_PIZZA_CUTTER = (By.XPATH, "//img[@title='The Pizza Cutter (Patan)']")

    MENU_SEARCH_BAR = (By.XPATH, "//input[@placeholder='Search food item']")

    DROPDOWN_SYANKO = (By.XPATH,"//span[normalize-space()='Syanko Katti Roll (Sankhamul)']/parent::div")

    SYANKO_CARD = (By.XPATH,"//img[@title='Syanko Katti Roll (Sankhamul)']")
