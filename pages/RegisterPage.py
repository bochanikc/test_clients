import allure

from locators import Register
from .BasePage import BasePage


class RegisterPage(BasePage):

    def located_regisrer_page(self):
        with allure.step("Проверяем, что находимся на странице заявок"):
            self._wait_for_visible(Register.register_page)
            self._wait_for_visible(Register.search_block)
            self._wait_for_visible(Register.logout_button)

    def logout_user(self):
        with allure.step("Выход за пользователя "):
            self._click(Register.logout_button)
