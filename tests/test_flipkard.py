import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.customize_product_add_to_card import CustomizeProductAddToCard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time 
# from pages.product_page import ProductPage
# from pages.cart_page import CartPage


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


@allure.feature("Open Website")
@allure.story("Check Google Home Page")
@allure.severity(allure.severity_level.CRITICAL)
def test_current_title(driver):
    assert driver.title == "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
def test_search_product(driver):
    home_page = HomePage(driver)
    search_results_page = SearchResultsPage(driver)
    home_page.search_product("Mobiles phone")
    assert driver.find_element(*search_results_page.FIRST_PRODUCT_XPATH).is_displayed()
    # home_page.go_back()

def test_filters_and_select_brand(driver,wait):
    home_page = HomePage(driver)
    search_results_page = SearchResultsPage(driver)
    search_results_page.sort_by_price_low_to_high(1)
    check_selected_value = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='_6tw8ju']"))).text
    assert check_selected_value == "₹10000-₹30000+"
    search_results_page.apply_brand_filters("Apple")
    assert driver.find_element(*search_results_page.FIRST_PRODUCT_XPATH).is_displayed()
    search_results_page.select_brand("Apple iPhone 14 (Starlight, 256 GB)")
    assert wait.until(EC.visibility_of_element_located(search_results_page.SELECTED_BRAND_CLASS_NAME)).is_displayed()

def test_selected_brand_and_custumize(driver,wait):
    customize_product = CustomizeProductAddToCard(driver)
    customize_product.select_color_and_storage()
    assert wait.until(EC.visibility_of_element_located(customize_product.SELECT_512GB_XPATH)).is_displayed()
    assert wait.until(EC.visibility_of_element_located(customize_product.SELECT_BRAND_COLORS_XPATH)).is_displayed()

def test_add_to_card(driver,wait):
    customize_product = CustomizeProductAddToCard(driver)
    customize_product.add_to_card()
    assert "Apple iPhone 14 (Starlight, 512 GB)" in customize_product.CARDS_LIST
    time.sleep(5)


