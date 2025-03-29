from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time 


class SearchResultsPage:
    FIRST_PRODUCT_XPATH = (By.CLASS_NAME, "KzDlHZ")
    FILTER_BRAND_XPATH = (By.XPATH, "(//div[contains(@class, '_6i1qKy')])[position() <= 7]")
    FILTER_PRICE_RANGE_XPATH = (By.XPATH, "//div[@class='suthUA']//select[@class='Gn+jFg']")
    SORT_DROPDOWN_XPATH = (By.CLASS_NAME, "_10UF8M")
    SORT_HIGH_TO_LOW_XPATH = (By.XPATH, "//div[text()='Price -- High to Low']")
    SELECT_BRAND_CLASS_NAME = (By.CLASS_NAME, "KzDlHZ")
    SELECTED_BRAND_CLASS_NAME = (By.CLASS_NAME, "VU-ZEz")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds

    def click_first_product(self):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_PRODUCT_XPATH)).click()

    def sort_by_price_high_to_low(self):
        self.wait.until(EC.element_to_be_clickable(self.SORT_DROPDOWN_XPATH)).click()
        self.wait.until(EC.element_to_be_clickable(self.SORT_HIGH_TO_LOW_XPATH)).click()

    def sort_by_price_low_to_high(self,option):
        dropdown = Select(self.wait.until(EC.presence_of_element_located(self.FILTER_PRICE_RANGE_XPATH)))
        if option == 1:
            dropdown.select_by_visible_text("₹10000")
        elif option == 2:
            dropdown.select_by_visible_text("₹20000")
        else:
            print("No option found")

    def apply_brand_filters(self,option):
        # brand_checkbox_values = self.driver.find_elements(*self.FILTER_BRAND_XPATH)
        brand_checkbox_values = self.wait.until(EC.presence_of_all_elements_located(self.FILTER_BRAND_XPATH))
        for checkbox in brand_checkbox_values:
            brand_text = checkbox.text
            if brand_text == option:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
                self.driver.execute_script("arguments[0].click();", checkbox)
                print(f"Successfully selected: {option}")
                return
        print(f"Brand '{option}' not found in available filters")

    def select_brand(self,option):
        time.sleep(3)
        iphone_options = self.wait.until(EC.presence_of_all_elements_located(self.SELECT_BRAND_CLASS_NAME))
        main_window = self.driver.current_window_handle
        for iphones in iphone_options:   
            iphones_text = iphones.text
            if iphones_text == option:
                iphones.click()
                print(f"Successfully selected: {option}")
                self.wait.until(lambda d: len(d.window_handles) > 1)
                for window in self.driver.window_handles:
                    if window != main_window:
                        self.driver.switch_to.window(window)
                        print("Switched to new window")
                        return
        print(f"Iphones '{option}' not found in available list")
