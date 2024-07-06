import allure

from pages.base_page import BasePage
from locators.locators import ForgotPasswordPageLocators as Fppl

from data import CommonData


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Checking the visibility of the specified order number')
    def send_user_email_and_click_recover(self):
        self.send_user_data(Fppl.email_entry_field_fpp, CommonData.test_email)
        self.click_element(Fppl.recover_button_fpp)

