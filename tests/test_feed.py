import allure
import pytest
import time

from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
from pages.history_page import HistoryPage
from locators.locators import MainPageLocators as Mpl
from locators.locators import ProfilePageLocators as Ppl
from locators.locators import FeedPageLocators as Fpl
from locators.locators import HistoryPageLocators as Hpl

from data import CommonData


class TestFeed:

    @allure.title('Checking the opening of the order details pop-up window')
    @allure.description('Checks that clicking on the order opens order details pop-up window')
    def test_click_on_order_opens_details_popup_window(self, driver, create_user, sign_in,
                                                       create_new_order_and_get_its_number):
        main_page = MainPage(driver)
        main_page.click_element(Mpl.feed_button_header)
        feed_page = FeedPage(driver)
        order_number = create_new_order_and_get_its_number
        feed_page.click_on_created_order(order_number)
        assert feed_page.check_element_is_visible(Fpl.composition_header), 'Order details window is not displayed'

    @allure.title('Checking that user orders from "Orders History" are displayed on "Feed page"')
    @allure.description('Checks that user orders from "Orders History" are displayed on "Feed page"')
    def test_user_order_displayed_on_feed_page(self, driver, create_user, sign_in):
        main_page = MainPage(driver)
        main_page.create_new_order()
        main_page.click_element(Mpl.account_button_header)
        profile_page = ProfilePage(driver)
        profile_page.click_element(Ppl.orders_history_url)
        history_page = HistoryPage(driver)
        order_number = history_page.get_text_element(Hpl.order_number_history)
        profile_page.click_element(Mpl.feed_button_header)
        feed_page = FeedPage(driver)
        assert feed_page.check_order_number_is_visible(order_number), \
            'User orders from "Orders History" are not displayed on "Feed page"'

    @allure.title('Checking increase of the counters')
    @allure.description('Parametrized test which checks that creating a new order increases the counters')
    @pytest.mark.parametrize('counter, description', CommonData.counters)
    def test_increase_completed_counters(self, driver, create_user, sign_in, counter, description):
        main_page = MainPage(driver)
        main_page.click_element(Mpl.feed_button_header)
        feed_page = FeedPage(driver)
        counter_prior_order = feed_page.get_text_element(counter)
        main_page.create_new_order()
        main_page.click_element(Mpl.feed_button_header)
        counter_after_order = feed_page.get_text_element(counter)
        assert counter_after_order > counter_prior_order, \
            f'"{description}" counter did not increase'

    @allure.title('Checking displaying the order number on the "In progress" section')
    @allure.description('Checks that after placing an order its number is displayed on the "In progress" section')
    def test_order_number_displayed_in_progress_section(self, driver, create_user, sign_in,
                                                        create_new_order_and_get_its_number):
        order_number = create_new_order_and_get_its_number
        main_page = MainPage(driver)
        main_page.click_element(Mpl.feed_button_header)
        feed_page = FeedPage(driver)
        feed_page.check_if_order_number_is_shown_in_progress()
        order_number_in_progress = feed_page.get_text_element(Fpl.in_progress_number)
        assert f'0{order_number}' == order_number_in_progress, \
            'Number of created order is not displayed in "In progress" section'