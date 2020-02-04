from locators import EmailSubmit
from selenium.webdriver.common.by import By


class EmailSubmitPage:

    def __init__(self, driver):
        self.driver = driver

    def located_email_submit_page(self):
        assert self.driver.find_element(By.CSS_SELECTOR, EmailSubmit.link_send_submit_again['css']).text == "нажмите здесь для повторной отправки"
