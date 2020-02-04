import random
import time

import pytest
from selenium.webdriver.common.by import By
from locators import EmailSubmit, Registration, Common
from pages import RegistrationPage, EmailSubmitPage
from pages.common import Alerts


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
        RegistrationPage(bro).registration_new_user(name, surname, email, company_name, password, phone)
        EmailSubmitPage(bro).located_email_submit_page()
        print('\n-------------------------------------------'
              + '\nemail: ' + email
              + '\nПароль: ' + password
              + '\n-------------------------------------------\n'
              + '\nИмя: ' + name
              + '\nФамилия: ' + surname
              + '\nИмя компании: ' + company_name
              + '\nТелефон: ' + str(phone))

    def test_empty_name_field(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        name, surname, email, company_name, password, phone = generate_test_data
        expected_fail_text = 'Поле имя обязательно для заполнения.'
        RegistrationPage(bro).registration_new_user('', surname, email, company_name, password, phone)
        Alerts(bro).check_fail_alert_of_field(expected_fail_text)
