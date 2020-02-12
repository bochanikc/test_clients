import allure
from locators import EmailSubmit
from .BasePage import BasePage


class EmailSubmitPage(BasePage):

    def located_email_submit_page(self):
        with allure.step("Проверяем, что находимся на странице подтверждения пароля "):
            self._wait_for_visible(EmailSubmit.image_email_submit)
            assert self._wait_for_visible(EmailSubmit.link_send_submit_again).text == "нажмите здесь для повторной отправки"
