from locators import Common
from selenium.webdriver.common.by import By


class Alerts:

    def __init__(self, driver):
        self.driver = driver

    def check_fail_alert_from_server_on_field(self, expected_fail_text):
        fail_text = self.driver.find_element(By.CSS_SELECTOR,
                                             Common.Alerts.FailMessage.fail_message_from_server['css']).text
        print(f"Ожидание: {expected_fail_text}\n"
              f"Реальность: {fail_text}")
        assert fail_text == expected_fail_text, "Ошибка не корректна"

    def check_fail_alert_from_front_on_field(self, expected_fail_text):
        fail_text = self.driver.find_element(By.CSS_SELECTOR,
                                             Common.Alerts.FailMessage.fail_message_on_front['css']).text
        print(f"Ожидание: {expected_fail_text}\n"
              f"Реальность: {fail_text}")
        assert fail_text == expected_fail_text, "Ошибка не корректна"

    def check_fail_other_alert(self, expected_fail_text):
        fail_text = self.driver.find_element(By.CSS_SELECTOR,
                                             Common.Alerts.FailMessage.fail_message['css']).text
        print(f"Ожидание: {expected_fail_text}\n"
              f"Реальность: {fail_text}")
        assert fail_text == expected_fail_text, "Ошибка не корректна"
