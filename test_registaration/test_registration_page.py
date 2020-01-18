import pytest
from selenium.webdriver.common.by import By

from locators.AutorizationPage import AutorizationPage
from locators.RegisterPage import RegisterPage
from locators.RegistrationPage import RegistrationPage



class TestRegistrationPage:

    def test_empty_name_field(self, browser, test_go_to_registration_page):
        pass

