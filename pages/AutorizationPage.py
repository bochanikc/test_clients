import allure
from selenium.webdriver.common.by import By
from locators import Autorization
from .BasePage import BasePage


class AutorizationPage(BasePage):

    def located_autorization_page(self):
        with allure.step("Проверяем, что находимся на странице авторизации "):
            self._wait_for_visible(Autorization.autorization_page)
            self._wait_for_visible(Autorization.email_field)
            self._wait_for_visible(Autorization.password_field)

    def auth_by_user(self, email, password):
        with allure.step(f"Авторизируемся за пользователя '{email}' / '{password}' "):
            self._input(Autorization.email_field, email)
            self._input(Autorization.password_field, password)
            self._click(Autorization.submit_button)

    def go_to_guest_code_page(self):
        with allure.step(f"Переходим на страницу 'вход по коду'"):
            self._click(Autorization.guest_code_page)

    def go_to_regitration_page_on_link(self, url):
        with allure.step("Проходим на страницу регистрации "):
            self.driver.find_element(By.CSS_SELECTOR, f".in3[href='{url}register']").click()

    def go_to_password_reset_page_on_link(self, url):
        with allure.step("Проходим на страницу 'Сбросить пароль' "):
            self.driver.find_element(By.CSS_SELECTOR, f".in3[href='{url}password/reset']").click()
