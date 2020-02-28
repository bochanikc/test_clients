import allure

from locators import SearchRequest
from .BasePage import BasePage


class SearchRequestPage(BasePage):

    def located_search_request_page(self):
        with allure.step("Проверяем, что находимся на странице заявок"):
            self._wait_for_visible(SearchRequest.search_request_page)
            self._wait_for_visible(SearchRequest.search_block)
            self._wait_for_visible(SearchRequest.logout_button)

    def logout_user(self):
        with allure.step("Выход за пользователя "):
            self._click(SearchRequest.logout_button)
