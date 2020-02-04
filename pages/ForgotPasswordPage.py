from locators import ForgotPassword
from selenium.webdriver.common.by import By


class ForgotPasswordPage:

    def __init__(self, driver):
        self.driver = driver

    def located_forgot_password_page(self):
        self.driver.find_element(By.CSS_SELECTOR, ForgotPassword.email_field['css'])
        self.driver.find_element(By.CSS_SELECTOR, ForgotPassword.submit_button['css'])
