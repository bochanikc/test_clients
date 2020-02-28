import allure
import pytest
from data_for_test import TestAccount
from pages import AutorizationPage, SearchRequestPage, RegistrationPage, ForgotPasswordPage, GuestCodePage
from pages.common import Alerts


@pytest.mark.smoke
@allure.feature('Авторизация')
@allure.severity(allure.severity_level.CRITICAL)
class TestAutorizationSmoke:

    @allure.story('Успешная авторизация')
    @pytest.fixture()
    def test_autorization_success(self, browser):
        bro = browser
        AutorizationPage(bro).auth_by_user(TestAccount.LOGIN, TestAccount.PASSWORD)
        SearchRequestPage(bro).located_search_request_page()

    @allure.story('Переход на страницу входа по коду')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_guest_code_page(self, browser):
        bro = browser
        AutorizationPage(bro).go_to_guest_code_page()
        GuestCodePage(bro).located_guest_code_page()

    @allure.story('Логаут')
    @allure.severity(allure.severity_level.NORMAL)
    def test_logout(self, browser, test_autorization_success):
        bro = browser
        #time.sleep(5)
        SearchRequestPage(bro).logout_user()
        AutorizationPage(bro).located_autorization_page()

    @allure.story('Переход на страницу регистрации')
    def test_go_to_registration_page(self, browser):
        bro = browser
        url = bro.current_url
        AutorizationPage(bro).go_to_regitration_page_on_link(url)
        RegistrationPage(bro).located_registration_page()

    @allure.story('Переход на страницу "Забыли пароль"')
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_forgot_password_page(self, browser):
        bro = browser
        url = bro.current_url
        AutorizationPage(bro).go_to_password_reset_page_on_link(url)
        ForgotPasswordPage(bro).located_forgot_password_page()


@allure.feature('Авторизация')
@allure.story('Ошибки в заполнении полей')
@allure.severity(allure.severity_level.MINOR)
class TestAutorizationFailFields:

    def test_autorization_email_empty_field(self, browser):
        bro = browser
        expected_fail_text = 'Поле электронный адрес обязательно для заполнения'
        AutorizationPage(bro).auth_by_user('', TestAccount.PASSWORD)
        Alerts(bro).check_fail_other_alert(expected_fail_text)

    def test_autorization_password_empty_field(self, browser):
        bro = browser
        expected_fail_text = 'Поле пароль обязательно для заполнения'
        AutorizationPage(bro).auth_by_user(TestAccount.LOGIN, '')
        Alerts(bro).check_fail_other_alert(expected_fail_text)

    def test_autorization_password_invalid(self, browser):
        bro = browser
        expected_fail_text = 'Имя пользователя и пароль не совпадают. Если вам в письме пришел код доступа, ' \
                             'перейдите по ссылке "Войти по коду доступа" над кнопкой "Войти"'
        AutorizationPage(bro).auth_by_user(TestAccount.LOGIN, TestAccount.PASSWORD + '21')
        Alerts(bro).check_fail_other_alert(expected_fail_text)

    def test_autorization_email_invalid(self, browser):
        bro = browser
        expected_fail_text = 'Имя пользователя и пароль не совпадают. Если вам в письме пришел код доступа, ' \
                             'перейдите по ссылке "Войти по коду доступа" над кнопкой "Войти"'
        AutorizationPage(bro).auth_by_user(TestAccount.LOGIN + '21', TestAccount.PASSWORD)
        Alerts(bro).check_fail_other_alert(expected_fail_text)
