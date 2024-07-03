from pages.base_page import BasePage
from locators.locators import ProfilePageLocators as Ppl
from locators.locators import MainPageLocators as Mpl
from locators.locators import LoginPageLocators as Lpl
from locators.locators import HistoryPageLocators as Hpl
import allure
class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Check visibility profile page url')
    def check_profile_url(self):
        self.check_element_is_visible(Ppl.profile_url)

    @allure.step('Click on oreder history')
    def click_on_order_history(self):
        self.click_element(Ppl.orders_history_url)


    @allure.step('Click exit button')
    def click_on_exit_button(self):
        self.click_element(Ppl.exit_button)

    @allure.step('Clicking on header')
    def click_on_header(self):
        self.click_element(Mpl.account_button_header)

    @allure.step('Check login page')
    def check_email_field(self):
        self.check_element_is_visible(Lpl.email_input_field)
        return True

    @allure.step('Get order number from hisory')
    def get_last_order_number(self):
        return self.get_text_element(Hpl.order_number_history)

    @allure.step('Open order hisory')
    def open_order_history(self):
        self.click_element(Ppl.orders_history_url)


