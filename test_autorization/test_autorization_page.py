import time
from selenium.webdriver.common.by import By
from locators import AutorizationPage, ForgotPassword, RegisterPage, RegistrationPage, FailMessage


class TestAutorizationRegress:

    def test_autorization_success(self, browser):
        bro = browser
        #Заполняем поля авторизации
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.email_field['css']).send_keys(
            'nfrolov@email.ru')
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.password_field['css']).send_keys('Qwerty123')
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.submit_button['css']).click()
        #Проверяем, что авторизировались
        bro.find_element(By.CSS_SELECTOR, RegisterPage.register_page['css'])
        bro.find_element(By.CSS_SELECTOR, RegisterPage.search_block['css'])
        bro.find_element(By.CSS_SELECTOR, RegisterPage.logout_button['css'])

    def test_logout(self, browser):
        bro = browser
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.email_field['css']).send_keys(
            'nfrolov@email.ru')
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.password_field['css']).send_keys('Qwerty123')
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.submit_button['css']).click()
        time.sleep(5)
        bro.find_element(By.CSS_SELECTOR, RegisterPage.logout_button['css']).click()
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.autorization_page['css'])
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.email_field['css'])
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.password_field['css'])

    def test_autorization_email_empty_field(self, browser):
        bro = browser
        expected_fail_text = 'Поле электронный адрес обязательно для заполнения.'
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.password_field['css']).send_keys('Qwerty123')
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.submit_button['css']).click()
        fail_text = bro.find_element(By.CSS_SELECTOR, FailMessage.fail_message['css']).text
        assert fail_text == expected_fail_text, "Ошибка не корректна"

    def test_autorization_password_empty_field(self, browser):
        bro = browser
        expected_fail_text = 'Поле пароль обязательно для заполнения.'
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.email_field['css']).send_keys(
            'nfrolov@email.ru')
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.submit_button)['css'].click()
        fail_text = bro.find_element(By.CSS_SELECTOR, FailMessage.fail_message['css']).text
        assert fail_text == expected_fail_text, "Ошибка не корректна"

    def test_autorization_password_invalid(self, browser):
        bro = browser
        expected_fail_text = 'Имя пользователя и пароль не совпадают.'
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.email_field['css']).send_keys(
            'nfrolov@email.ru')
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.password_field['css']).send_keys(
            'Qwerty123' + '21')
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.submit_button['css']).click()
        fail_text = bro.find_element(By.CSS_SELECTOR, FailMessage.fail_message['css']).text
        assert fail_text == expected_fail_text, "Ошибка не корректна"

    def test_autorization_email_invalid(self, browser):
        bro = browser
        expected_fail_text = 'Имя пользователя и пароль не совпадают.'
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.email_field['css']).send_keys(
            'nfrolov@email.ru' + '21')
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.password_field['css']).send_keys('Qwerty123')
        bro.find_element(By.CSS_SELECTOR, AutorizationPage.submit_button['css']).click()
        fail_text = bro.find_element(By.CSS_SELECTOR, FailMessage.fail_message['css']).text
        assert fail_text == expected_fail_text, "Ошибка не корректна"

    def test_go_to_registration_page(self, browser):
        bro = browser
        url = bro.current_url
        bro.find_element(By.CSS_SELECTOR, f".in3[href='{url}register']").click()
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.name_field['css'])
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.submit_button['css'])
        bro.find_element(By.CSS_SELECTOR, RegistrationPage.rocket_image['css'])

    def test_go_to_forgot_password_page(self, browser):
        bro = browser
        url = bro.current_url
        bro.find_element(By.CSS_SELECTOR, f".in3[href='{url}password/reset']").click()
        bro.find_element(By.CSS_SELECTOR, ForgotPassword.email_field['css'])
        bro.find_element(By.CSS_SELECTOR, ForgotPassword.submit_button['css'])
