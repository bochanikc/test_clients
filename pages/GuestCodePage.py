import allure

from locators import GuestCode
from .BasePage import BasePage


class GuestCodePage(BasePage):

    def located_guest_code_page(self):
        with allure.step("Проверяем, что находимся на странице входа по коду"):
            self._wait_for_visible(GuestCode.submit_button)
            self._wait_for_visible(GuestCode.code_field)
            self._wait_for_visible(GuestCode.picture)

    def auth_by_guest_with_code(self, clients_code):
        with allure.step(f"Заходим по коду заявки: {clients_code}"):
            self._input(GuestCode.code_field, clients_code)
            self._click(GuestCode.submit_button)
    