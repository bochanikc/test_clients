from locators import EmailSubmit
from selenium.webdriver.common.by import By
from .BasePage import BasePage


class EmailSubmitPage(BasePage):

    def located_email_submit_page(self):
        assert self._wait_for_visible(EmailSubmit.link_send_submit_again).text == "нажмите здесь для повторной отправки"
