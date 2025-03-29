from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    # Locators
    SEARCH_BOX_XPATH = (By.NAME, "q")
    SEARCH_BUTTON_XPATH = (By.XPATH, "//button[@title='Search for Products, Brands and More']")
    CLOSE_BUTTON_XPATH = (By.XPATH, "//button[contains(text(),'✕')]")
    LOGIN_BUTTON_XPATH = (By.XPATH, "//a[normalize-space()='Login']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds

    def search_product(self, product_name):
        search_box = self.wait.until(EC.visibility_of_element_located(self.SEARCH_BOX_XPATH))
        search_box.clear()
        search_box.send_keys(product_name)
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON_XPATH)).click()

    def go_back(self):
        self.driver.back()

    def close_logout(self):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON_XPATH)).click()
        close_button = self.wait.until(EC.visibility_of_element_located(self.CLOSE_BUTTON_XPATH))
        print(close_button.text)
        close_button.click()


    