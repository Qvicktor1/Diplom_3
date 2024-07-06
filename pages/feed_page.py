import allure

from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage
from locators.locators import FeedPageLocators as Fpl


class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Clicking on the specified order number')
    def click_on_created_order(self, order_number):
        order_number_template = Fpl.order_number_template
        locator = (order_number_template[0], order_number_template[1].replace('#', f'#0{order_number}'))
        self.check_element_is_visible(locator).click()

    @allure.step('Checking the visibility of the specified order number')
    def check_order_number_is_visible(self, order_number):
        order_number_template = Fpl.order_number_template
        locator = (order_number_template[0], order_number_template[1].replace('#', f'{order_number}'))
        return self.check_element_is_visible(locator)

    @allure.step('Checking that line "All orders are ready" in "In progress" section '
                 'has changed to current order number')
    def check_if_order_number_is_shown_in_progress(self):
        self.wait_till_text_is_shown(Fpl.in_progress_number, '0')

    @allure.step('Get in progress number')
    def get_in_progress_number(self):
        return self.get_text_element(Fpl.in_progress_number)

    @allure.step('Check order window opened')
    def check_order_window_opened(self):
        return self.check_element_is_visible(Fpl.composition_header)
