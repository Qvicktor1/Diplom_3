import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators as Mpl


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Clicking on the specified element')
    def close_order_modal(self):
        self.check_element_is_absent(Mpl.modal_overlay)
        self.click_element(Mpl.order_number_window_close_button)

    @allure.step('Creating a new order')
    def create_new_order(self):
        self.click_element(Mpl.constructor_button_header)
        self.drag_and_drop_element(Mpl.ingredient_name, Mpl.constructor_upper_bun_placeholder)
        self.drag_and_drop_element(Mpl.fluoric_bun_name, Mpl.constructor_upper_bun_placeholder)
        self.click_element(Mpl.place_order_button)
        self.click_element(Mpl.order_number_window_close_button)

    @allure.step('Checking that created order number is shown in confirmation order window')
    def check_if_created_order_number_is_shown(self):
        self.check_element_is_visible(Mpl.order_loading_animation)
        self.check_element_is_absent(Mpl.order_loading_animation)

    @allure.step('Click on bun')
    def click_fluoric_bun(self):
        self.click_element(Mpl.fluoric_bun_name)

    @allure.step('Check open bun details')
    def check_open_details(self):
        return self.check_element_is_visible(Mpl.ingredient_details_header)

    @allure.step('Check absent button')
    def check_absent_button(self):
        return self.check_element_is_absent(Mpl.ingredient_details_close_button)

    @allure.step('Close details')
    def close_details(self):
        self.click_element(Mpl.ingredient_details_close_button)

    @allure.step('check order history')
    def check_order_history(self):
        return self.check_element_is_visible(Mpl.order_identifier_header)

    @allure.step('check open password page')
    def check_password_page(self):
        return self.check_element_is_visible(Mpl.show_password_button)

    @allure.step('show password')
    def show_password(self):
        return self.click_element(Mpl.show_password_button)

    @allure.step('check highlight password')
    def check_highlight_password(self):
        return self.check_element_is_visible(Mpl.password_field_highlight)

    @allure.step('Clicking on account')
    def click_on_account_button(self):
        self.click_element(Mpl.account_button_header)

    @allure.step('Clicking on feed')
    def click_on_feed_button(self):
        self.click_element(Mpl.feed_button_header)

