import time
import pytest
from pages import AutorizationPage, RegisterPage, RegistrationPage, ForgotPasswordPage
from pages.common import Alerts


class TestAutorizationRegress:

    @pytest.mark.smoke
    def test_autorization_success(self, browser):
        bro = browser
        AutorizationPage(bro).auth_by_user('nfrolov@email.ru', 'Qwerty123')
        RegisterPage(bro).located_regisrer_page()

    @pytest.mark.smoke
    def test_logout(self, browser):
        bro = browser
        AutorizationPage(bro).auth_by_user('nfrolov@email.ru', 'Qwerty123')
        time.sleep(5)
        RegisterPage(bro).logout_user()
        AutorizationPage(bro).located_autorization_page()

    def test_autorization_email_empty_field(self, browser):
        bro = browser
        expected_fail_text = 'Поле электронный адрес обязательно для заполнения'
        AutorizationPage(bro).auth_by_user('', 'Qwerty123')
        Alerts(bro).check_fail_alert_of_field(expected_fail_text)

    def test_autorization_password_empty_field(self, browser):
        bro = browser
        expected_fail_text = 'Поле пароль обязательно для заполнения'
        AutorizationPage(bro).auth_by_user('nfrolov@email.ru', '')
        Alerts(bro).check_fail_alert_of_field(expected_fail_text)

    def test_autorization_password_invalid(self, browser):
        bro = browser
        expected_fail_text = 'Имя пользователя и пароль не совпадают'
        AutorizationPage(bro).auth_by_user('nfrolov@email.ru', 'Qwerty123'+'21')
        Alerts(bro).check_fail_alert_of_field(expected_fail_text)

    def test_autorization_email_invalid(self, browser):
        bro = browser
        expected_fail_text = 'Имя пользователя и пароль не совпадают'
        AutorizationPage(bro).auth_by_user('nfrolov@email.ru'+'21', 'Qwerty123')
        Alerts(bro).check_fail_alert_of_field(expected_fail_text)

    @pytest.mark.smoke
    def test_go_to_registration_page(self, browser):
        bro = browser
        url = bro.current_url
        AutorizationPage(bro).go_to_regitration_page_on_link(url)
        RegistrationPage(bro).located_registration_page()

    @pytest.mark.smoke
    def test_go_to_forgot_password_page(self, browser):
        bro = browser
        url = bro.current_url
        AutorizationPage(bro).go_to_password_reset_page_on_link(url)
        ForgotPasswordPage(bro).located_forgot_password_page()
