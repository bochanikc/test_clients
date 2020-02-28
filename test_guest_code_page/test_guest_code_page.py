import allure
import pytest

from pages import GuestCodePage, RequestGroupPage
from data_for_test import TestAccount


@pytest.mark.smoke
@allure.feature('Авторизация по коду')
@allure.severity(allure.severity_level.CRITICAL)
class TestGuestCodePageSmoke:

    def test_autorization_with_guest_code(self, browser, test_go_to_guest_code_page):
        bro = browser
        GuestCodePage(bro).auth_by_guest_with_code(TestAccount.CLIENT_CODE)
        RequestGroupPage(bro).located_request_group_page()
