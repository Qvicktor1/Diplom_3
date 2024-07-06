from pages.base_page import BasePage
from locators.locators import ProfilePageLocators as Ppl
import allure
class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Check visibility profile page url')
    def check_profile_url(self):
        return self.check_element_is_visible(Ppl.profile_url)

    @allure.step('Click on oreder history')
    def click_on_order_history(self):
        self.click_element(Ppl.orders_history_url)

    @allure.step('Click exit button')
    def click_on_exit_button(self):
        self.click_element(Ppl.exit_button)

    @allure.step('Check login page')
    def check_email_field(self):
        self.check_element_is_visible(Ppl.email_input_field)
        return True

    @allure.step('Get order number from history')
    def get_last_order_number(self):
        return self.get_text_element(Ppl.order_number_history)

    @allure.step('Open order history')
    def open_order_history(self):
        self.click_element(Ppl.orders_history_url)


