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
        Wait(self.driver, timeout=10).until(ec.visibility_of_element_located(locator)).click()

    @allure.step('Checking the visibility of the specified order number')
    def check_order_number_is_visible(self, order_number):
        order_number_template = Fpl.order_number_template
        locator = (order_number_template[0], order_number_template[1].replace('#', f'{order_number}'))
        return Wait(self.driver, timeout=10).until(ec.visibility_of_element_located(locator))

    @allure.step('Checking that line "All orders are ready" in "In progress" section '
                 'has changed to current order number')
    def check_if_order_number_is_shown_in_progress(self):
        self.wait_till_text_is_shown(Fpl.in_progress_number, '0')

    @allure.step('Get in progress number')
    def get_in_progress_number(self):
        return self.get_text_element(Fpl.in_progress_number)
