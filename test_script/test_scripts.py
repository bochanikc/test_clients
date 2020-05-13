import pytest
from pages import RegistrationPage, EmailSubmitPage
from pages.common import Alerts
from data_for_test import TestAccount

@pytest.mark.skip
class TestFirstScripts:

    def test_registration_user_for_autotests(self, browser, test_go_to_registration_page):
        bro = browser
        name, surname, email, password, confirm_password, phone = TestAccount.NAME, TestAccount.SURNAME, \
                                                                  TestAccount.LOGIN, TestAccount.PASSWORD, \
                                                                  TestAccount.PASSWORD, TestAccount.PHONE_NUMBER
        print(phone)
        RegistrationPage(bro).registration_new_user(name, surname, email, password, confirm_password, phone)
        EmailSubmitPage(bro).located_email_submit_page()
        print('\n-------------------------------------------'
              + '\nemail: ' + email
              + '\nПароль: ' + password
              + '\n-------------------------------------------\n'
              + '\nИмя: ' + name
              + '\nФамилия: ' + surname
              + '\nТелефон: ' + str(phone))
