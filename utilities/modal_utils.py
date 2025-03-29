from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def close_login_modal(driver):
    try:
        close_button = (By.CLASS_NAME, "QqFHMw NEEcDr")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(close_button)).click()
        print("Login modal closed successfully.")
    except Exception as e:
        print("Login modal not found or already closed.")