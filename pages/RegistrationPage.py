from locators import Registration
from selenium.webdriver.common.by import By


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    def located_registration_page(self):
        self.driver.find_element(By.CSS_SELECTOR, Registration.name_field['css'])
        self.driver.find_element(By.CSS_SELECTOR, Registration.submit_button['css'])
        self.driver.find_element(By.CSS_SELECTOR, Registration.rocket_image['css'])

    def registration_new_user(self, name, surname, email, company_name, password, phone):
        self.driver.find_element(By.CSS_SELECTOR, Registration.name_field['css']).send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, Registration.surname_field['css']).send_keys(surname)
        self.driver.find_element(By.CSS_SELECTOR, Registration.email_field['css']).send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, Registration.company_name_field['css']).send_keys(company_name)
        self.driver.find_element(By.CSS_SELECTOR, Registration.password_field['css']).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, Registration.password_confirm_field['css']).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, Registration.phone_field['css']).click()
        self.driver.find_element(By.CSS_SELECTOR, Registration.phone_field['css']).send_keys(phone)
        # bro.find_element(By.CSS_SELECTOR, RegistrationPage.news_subscribe_checkbox_check).click()
        button = self.driver.find_element(By.CSS_SELECTOR, Registration.submit_button['css'])
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
