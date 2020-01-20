import random
import time

import pytest
from selenium.webdriver.common.by import By
from locators.RegistrationPage import RegistrationPage


class TestRegistrationPage:
    now_time = int(time.time())
    name = "Имяселениумтест" + str(now_time)
    surname = "Фамилия" + str(now_time)
    email = "email" + str(now_time) + "@email.com"
    company_name = "Company Selenium " + str(now_time) + " inc."
    password = "Qwerty123"
    phone = random.randint(1000000000, 9999999999)

    def test_registration_success(self, browser, test_go_to_registration_page):
        bro = browser
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.name_field).send_keys(self.name)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.surname_field).send_keys(self.surname)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.email_field).send_keys(self.email)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.company_name_field).send_keys(self.company_name)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.password_field).send_keys(self.password)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.password_confirm_field).send_keys(self.password)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.phone_field).send_keys(self.phone)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.news_subscribe_checkbox_click).click()
        time.sleep(5)
        pass

    def test_empty_name_field(self, browser, test_go_to_registration_page):
        bro = browser
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.name_field).send_keys("sdfgdrfg")
        pass
