from locators import Registration
from .BasePage import BasePage


class RegistrationPage(BasePage):

    def located_registration_page(self):
        self._wait_for_visible(Registration.name_field)
        self._wait_for_visible(Registration.submit_button)
        self._wait_for_visible(Registration.rocket_image)

    def registration_new_user(self, name, surname, email, company_name, password, confirm_password, phone):
        self._input(Registration.name_field, name)
        self._input(Registration.surname_field, surname)
        self._input(Registration.email_field, email)
        self._input(Registration.company_name_field, company_name)
        self._input(Registration.password_field, password)
        self._input(Registration.password_confirm_field, confirm_password)
        self._input(Registration.phone_field, phone)
        #self._click(Registration.news_subscribe_checkbox_check)
        self._click(Registration.submit_button)
