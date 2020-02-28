import allure
import pytest
from pages import RegistrationPage, EmailSubmitPage
from pages.common import Alerts


@pytest.mark.smoke
@allure.feature('Регистрация')
@allure.story('Успешная регистрация')
@allure.severity(allure.severity_level.CRITICAL)
class TestRegistrationPageSmoke:

    def test_registration_success(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        name, surname, email, password, confirm_password, phone = generate_test_data
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


@allure.feature('Регистрация')
@allure.story('Ошибки в заполнении полей')
@allure.severity(allure.severity_level.MINOR)
class TestRegistrationPageRegress:

    def test_empty_name_field(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        expected_fail_text = 'Поле имя обязательно для заполнения'
        name, surname, email, password, confirm_password, phone = generate_test_data
        RegistrationPage(bro).registration_new_user('', surname, email, password, confirm_password, phone)
        Alerts(bro).check_fail_alert_from_server_on_field(expected_fail_text)

    def test_empty_surname_field(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        expected_fail_text = 'Поле фамилия обязательно для заполнения'
        name, surname, email, password, confirm_password, phone = generate_test_data
        RegistrationPage(bro).registration_new_user(name, '', email, password, confirm_password, phone)
        Alerts(bro).check_fail_alert_from_server_on_field(expected_fail_text)

    def test_empty_email_field(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        expected_fail_text = 'Поле электронный адрес обязательно для заполнения'
        name, surname, email, password, confirm_password, phone = generate_test_data
        RegistrationPage(bro).registration_new_user(name, surname, '', password, confirm_password, phone)
        Alerts(bro).check_fail_alert_from_server_on_field(expected_fail_text)


    def test_empty_password_field(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        expected_fail_text = 'Поле пароль обязательно для заполнения'
        name, surname, email, password, confirm_password, phone = generate_test_data
        RegistrationPage(bro).registration_new_user(name, surname, email, '', confirm_password, phone)
        Alerts(bro).check_fail_alert_from_server_on_field(expected_fail_text)

    @pytest.mark.parametrize('password_param, expected_fail_text',
                             [
                                 ('12345', 'Количество символов в поле пароль должно быть не менее 8'),
                                 ('Qwerty', 'Количество символов в поле пароль должно быть не менее 8'),
                                 ('Qwerty1', 'Количество символов в поле пароль должно быть не менее 8'),
                                 ('Qwertyui', 'Поле пароль имеет ошибочный формат')
                             ])
    def test_incorrect_password_field(self, browser, test_go_to_registration_page, generate_test_data,
                                      password_param, expected_fail_text):
        bro = browser
        name, surname, email, password, confirm_password, phone = generate_test_data
        password = password_param
        confirm_password = password_param
        RegistrationPage(bro).registration_new_user(name, surname, email, password, confirm_password, phone)
        Alerts(bro).check_fail_alert_from_server_on_field(expected_fail_text)

    def test_incorrect_email_field(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        expected_fail_text = 'Поле электронный адрес должно быть действительным электронным адресом'
        name, surname, email, password, confirm_password, phone = generate_test_data
        email = email[0:len(email) - 10]
        RegistrationPage(bro).registration_new_user(name, surname, email, password, confirm_password, phone)
        Alerts(bro).check_fail_alert_from_server_on_field(expected_fail_text)
