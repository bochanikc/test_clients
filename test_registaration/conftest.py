import random
import time
import pytest
from pages import AutorizationPage, RegistrationPage


@pytest.fixture(scope="function")
def test_go_to_registration_page(browser):
    bro = browser
    url = bro.current_url
    AutorizationPage(bro).go_to_regitration_page_on_link(url)
    RegistrationPage(bro).located_registration_page()


@pytest.fixture()
def generate_test_data():
    now_time = str(int(time.time()))
    name = "Имяселениумтест" + now_time
    surname = "Фамилия" + now_time
    email = "email" + now_time + "@email.com"
    password = "Qwerty123"
    phone = random.randint(1000000000, 9999999999)
    return name, surname, email, password, password, phone

