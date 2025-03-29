from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time 


class CustomizeProductAddToCard:
    SELECT_512GB_XPATH = (By.XPATH, "//a[normalize-space()='512 GB']")
    SELECT_BRAND_COLORS_XPATH = (By.XPATH, "//a[@class='GK7Ljp io5kcR']")
    SELECT_COLOR_ELEMENTS = (By.CLASS_NAME, "_0QyAeO")
    SELECTED_BRAND_CLASS_NAME = (By.CLASS_NAME, "VU-ZEz")
    ADD_TO_CARD_XPATH = (By.XPATH,"//button[normalize-space()='Add to cart']")
    CARDS_LIST_XPATH = (By.XPATH, "//div[contains(@class, 'gE4Hlh')]//a")
    CARDS_LIST = []


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)  # Wait for up to 10 seconds


    def select_color_and_storage(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_512GB_XPATH)).click()
        self.wait.until(EC.element_to_be_clickable(self.SELECT_BRAND_COLORS_XPATH)).click()

    def add_to_card(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CARD_XPATH)).click()
        card_list_element = self.wait.until(EC.presence_of_all_elements_located(self.CARDS_LIST_XPATH))
        for card in card_list_element:
            self.CARDS_LIST.append(card.text)
