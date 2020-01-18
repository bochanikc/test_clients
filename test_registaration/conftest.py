import pytest
from selenium.webdriver.common.by import By

from locators.RegistrationPage import RegistrationPage


@pytest.fixture(scope="function")
def test_go_to_registration_page(browser):
    bro = browser
    url = bro.current_url
    bro.find_element(By.CSS_SELECTOR, f".in3[href='{url}register']").click()
    bro.find_element(By.CSS_SELECTOR, RegistrationPage.name_field)
    bro.find_element(By.CSS_SELECTOR, RegistrationPage.submit_button)
