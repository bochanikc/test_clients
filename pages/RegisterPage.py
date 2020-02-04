from selenium.webdriver.common.by import By
from locators import Register

class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    def located_regisrer_page(self):
        self.driver.find_element(By.CSS_SELECTOR, Register.register_page['css'])
        self.driver.find_element(By.CSS_SELECTOR, Register.search_block['css'])
        self.driver.find_element(By.CSS_SELECTOR, Register.logout_button['css'])

    def logout_user(self):
        self.driver.find_element(By.CSS_SELECTOR, Register.logout_button['css']).click()
