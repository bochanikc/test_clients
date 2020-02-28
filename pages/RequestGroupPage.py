import allure

from locators import RequestGroup
from .BasePage import BasePage


class RequestGroupPage(BasePage):

    def located_request_group_page(self):
        with allure.step("Проверяем, что находимся на странице групп заявки"):
            self._wait_for_visible(RequestGroup.picture)
            self._wait_for_visible(RequestGroup.company_name)
            self._wait_for_visible(RequestGroup.group_card)
