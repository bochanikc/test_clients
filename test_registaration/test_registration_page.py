import pytest
from pages import RegistrationPage, EmailSubmitPage
from pages.common import Alerts


class TestRegistrationPage:

    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_registration_success(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        name, surname, email, company_name, password, confirm_password, phone = generate_test_data
        RegistrationPage(bro).registration_new_user(name, surname, email, company_name, password, confirm_password,
                                                    phone)
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
        name, surname, email, company_name, password, confirm_password, phone = generate_test_data
        expected_fail_text = 'Поле имя обязательно для заполнения'
        RegistrationPage(bro).registration_new_user('', surname, email, company_name, password, confirm_password, phone)
        Alerts(bro).check_fail_alert_of_field(expected_fail_text)

    def test_empty_surname_field(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        name, surname, email, company_name, password, confirm_password, phone = generate_test_data
        expected_fail_text = 'Поле фамилия обязательно для заполнения'
        RegistrationPage(bro).registration_new_user(name, '', email, company_name, password, confirm_password, phone)
        Alerts(bro).check_fail_alert_of_field(expected_fail_text)

    def test_empty_email_field(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        name, surname, email, company_name, password, confirm_password, phone = generate_test_data
        expected_fail_text = 'Поле электронный адрес обязательно для заполнения'
        RegistrationPage(bro).registration_new_user(name, surname, '', company_name, password, confirm_password, phone)
        Alerts(bro).check_fail_alert_of_field(expected_fail_text)

    def test_empty_company_field(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        name, surname, email, company_name, password, confirm_password, phone = generate_test_data
        expected_fail_text = 'Поле название компании обязательно для заполнения'
        RegistrationPage(bro).registration_new_user(name, surname, email, '', password, confirm_password, phone)
        Alerts(bro).check_fail_alert_of_field(expected_fail_text)

    def test_empty_password_field(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        name, surname, email, company_name, password, confirm_password, phone = generate_test_data
        expected_fail_text = 'Поле пароль обязательно для заполнения'
        RegistrationPage(bro).registration_new_user(name, surname, email, company_name, '', confirm_password, phone)
        Alerts(bro).check_fail_alert_of_field(expected_fail_text)

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
        name, surname, email, company_name, password, confirm_password, phone = generate_test_data
        password = password_param
        confirm_password = password_param
        RegistrationPage(bro).registration_new_user(name, surname, email, company_name,
                                                    password, confirm_password, phone)
        Alerts(bro).check_fail_alert_of_field(expected_fail_text)

    def test_incorrect_email_field(self, browser, test_go_to_registration_page, generate_test_data):
        bro = browser
        name, surname, email, company_name, password, confirm_password, phone = generate_test_data
        expected_fail_text = 'Поле электронный адрес должно быть действительным электронным адресом'
        email = email[0:len(email) - 10]
        RegistrationPage(bro).registration_new_user(name, surname, email, company_name,
                                                    password, confirm_password, phone)
        Alerts(bro).check_fail_alert_of_field(expected_fail_text)
