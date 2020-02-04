from locators import Register
from .BasePage import BasePage


class RegisterPage(BasePage):

    def located_regisrer_page(self):
        self._wait_for_visible(Register.register_page)
        self._wait_for_visible(Register.search_block)
        self._wait_for_visible(Register.logout_button)

    def logout_user(self):
        self._click(Register.logout_button)
