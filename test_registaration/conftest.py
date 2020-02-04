import pytest
from pages import AutorizationPage, RegistrationPage


@pytest.fixture(scope="function")
def test_go_to_registration_page(browser):
    bro = browser
    url = bro.current_url
    AutorizationPage(bro).go_to_regitration_page_on_link(url)
    RegistrationPage(bro).located_registration_page()
