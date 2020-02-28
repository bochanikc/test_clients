import pytest

from pages import AutorizationPage, GuestCodePage


@pytest.fixture(scope="function")
def test_go_to_guest_code_page(browser):
    bro = browser
    AutorizationPage(bro).go_to_guest_code_page()
    GuestCodePage(bro).located_guest_code_page()
