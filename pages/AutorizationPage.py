from selenium.webdriver.common.by import By
from locators import Autorization

class AutorizationPage:

    def __init__(self, driver):
        self.driver = driver

    def located_autorization_page(self):
        self.driver.find_element(By.CSS_SELECTOR, Autorization.autorization_page['css'])
        self.driver.find_element(By.CSS_SELECTOR, Autorization.email_field['css'])
        self.driver.find_element(By.CSS_SELECTOR, Autorization.password_field['css'])

    def auth_by_user(self, email, password):
        self.driver.find_element(By.CSS_SELECTOR, Autorization.email_field['css']).send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, Autorization.password_field['css']).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, Autorization.submit_button['css']).click()

    def go_to_regitration_page_on_link(self, url):
        self.driver.find_element(By.CSS_SELECTOR, f".in3[href='{url}register']").click()

    def go_to_password_reset_page_on_link(self, url):
        self.driver.find_element(By.CSS_SELECTOR, f".in3[href='{url}password/reset']").click()
