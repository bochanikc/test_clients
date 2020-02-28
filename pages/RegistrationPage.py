import allure
from locators import Registration
from .BasePage import BasePage


class RegistrationPage(BasePage):

    def located_registration_page(self):
        with allure.step("Проверяем, что находимся на странице регистрации "):
            self._wait_for_visible(Registration.name_field)
            self._wait_for_visible(Registration.surname_field)
            self._wait_for_visible(Registration.email_field)
            self._wait_for_visible(Registration.password_field)
            self._wait_for_visible(Registration.password_confirm_field)
            self._wait_for_visible(Registration.phone_field)
            self._wait_for_visible(Registration.news_subscribe_checkbox_check)
            self._wait_for_visible(Registration.submit_button)

    def registration_new_user(self, name, surname, email, password, confirm_password, phone):
        with allure.step("Регистрируем нового пользователя "):
            self._input(Registration.name_field, name)
            self._input(Registration.surname_field, surname)
            self._input(Registration.email_field, email)
            self._input(Registration.password_field, password)
            self._input(Registration.password_confirm_field, confirm_password)
            self._input(Registration.phone_field, phone)
            # self._click(Registration.news_subscribe_checkbox_check)
            self._click(Registration.submit_button)
            allure.attach('\nemail: ' + email
                          + '\nПароль: ' + password
                          + '\n-------------------------------------------\n'
                          + '\nИмя: ' + name
                          + '\nФамилия: ' + surname
                          + '\nТелефон: ' + str(phone),
                          'Тестовые данные: ')
