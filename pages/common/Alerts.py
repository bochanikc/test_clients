from locators import Common
from selenium.webdriver.common.by import By


class Alerts:

    def __init__(self, driver):
        self.driver = driver

    def check_fail_alert_of_field(self, expected_fail_text):
        fail_text = self.driver.find_element(By.CSS_SELECTOR, Common.Alerts.FailMessage.fail_message['css']).text
        assert fail_text == expected_fail_text, "Ошибка не корректна"
