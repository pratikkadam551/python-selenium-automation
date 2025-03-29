import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from utilities.common_utils import load_config
import time

@pytest.fixture(scope="session")
def config():
    return load_config()

@pytest.fixture(scope="session")
def driver(config):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(config["base_url"])  # Set up the base URL once
    yield driver
    driver.quit()  # Teardown: Close the browser after tests


@pytest.fixture()  # This fixture will run before every test case
def close_login_modal_globally(driver):
    try:
        close_button = (By.XPATH, "//span[@role='button' and @class='_30XB9F']")
        print("Waiting for login modal...")
        print(close_button.text)
        close_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(close_button))
        print("Login modal found. Attempting to close it...")
        driver.execute_script("arguments[0].click();", close_element)
        print("Login modal closed successfully.")
    except Exception as e:
        print("Login modal not found or already closed.")