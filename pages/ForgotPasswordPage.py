import allure
from locators import ForgotPassword
from .BasePage import BasePage


class ForgotPasswordPage(BasePage):

    def located_forgot_password_page(self):
        with allure.step("проверяем, что находимся на странице 'Забыли пароль' "):
            self._wait_for_visible(ForgotPassword.email_field)
            self._wait_for_visible(ForgotPassword.submit_button)
