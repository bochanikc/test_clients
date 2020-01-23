import random
import time

import pytest
from selenium.webdriver.common.by import By

from locators.EmailSubmitPage import EmailSubmitPage
from locators.RegistrationPage import RegistrationPage, FailMessage

@pytest.fixture()
def generate_test_data():
    now_time = str(int(time.time()))
    name = "Имяселениумтест" + now_time
    surname = "Фамилия" + now_time
    email = "email" + now_time + "@email.com"
    company_name = "Company Selenium " + now_time + " inc."
    password = "Qwerty123"
    phone = random.randint(1000000000, 9999999999)
    return name, surname, email, company_name, password, phone

class TestRegistrationPage:

    def test_registration_success(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        name, surname, email, company_name, password, phone = generate_test_data

        bro.find_element(By.CSS_SELECTOR, RegistrationPage.name_field).send_keys(name)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.surname_field).send_keys(surname)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.email_field).send_keys(email)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.company_name_field).send_keys(company_name)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.password_field).send_keys(password)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.password_confirm_field).send_keys(password)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.phone_field).click()
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.phone_field).send_keys(phone)
        # bro.find_element(By.CSS_SELECTOR, RegistrationPage.news_subscribe_checkbox_check).click()
        button = bro.find_element(By.CSS_SELECTOR, RegistrationPage.submit_button)
        bro.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        assert bro.find_element(By.CSS_SELECTOR,
                                EmailSubmitPage.link_send_submit_again).text == "нажмите здесь для повторной отправки"

    def test_empty_name_field(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        name, surname, email, company_name, password, phone = generate_test_data
        expected_fail_text = 'Поле имя обязательно для заполнения.'

        bro.find_element(By.CSS_SELECTOR, RegistrationPage.surname_field).send_keys(surname)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.email_field).send_keys(email)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.company_name_field).send_keys(company_name)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.password_field).send_keys(password)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.password_confirm_field).send_keys(password)
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.phone_field).click()
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.phone_field).send_keys(phone)
        # bro.find_element(By.CSS_SELECTOR, RegistrationPage.news_subscribe_checkbox_check).click()
        button = bro.find_element(By.CSS_SELECTOR, RegistrationPage.submit_button)
        bro.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

        fail_text = bro.find_element(By.CSS_SELECTOR, FailMessage.fail_message).text
        assert fail_text == expected_fail_text, "Ошибка не корректна"
