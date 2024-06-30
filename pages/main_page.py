import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators as Mpl


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Creating a new order')
    def create_new_order(self):
        self.click_element(Mpl.constructor_button_header)
        self.drag_and_drop_element(Mpl.ingredient_name, Mpl.constructor_upper_bun_placeholder)
        self.drag_and_drop_element(Mpl.fluoric_bun_name, Mpl.constructor_upper_bun_placeholder)
        self.click_element(Mpl.place_order_button)
        self.click_element(Mpl.order_number_window_close_button)

    @allure.step('Checking that created order number is shown in confirmation order window')
    def check_if_created_order_number_is_shown(self):
        self.wait_till_text_is_shown(Mpl.order_number, '0')