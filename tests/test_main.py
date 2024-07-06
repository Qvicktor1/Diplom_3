import allure
import pytest

from pages.main_page import MainPage
from locators.locators import MainPageLocators as Mpl

from data import CommonData


class TestMain:

    @allure.title('Checking the transition to the "Constructor" or "Feed" pages')
    @allure.description('Parametrized test which tests that clicking '
                        'on the "Constructor" or "Feed" header buttons leads '
                        'to the "Constructor" or "Feed" page correspondingly')
    @pytest.mark.parametrize('page_locator, page_header, description', CommonData.headers)
    def test_transition_to_constructor_and_feed_pages(self, driver, page_locator, page_header, description):
        main_page = MainPage(driver)
        main_page.click_on_account_button()
        main_page.click_element(page_locator)
        assert main_page.check_element_is_visible(page_header), \
            f'Unable to open "{description}" page'

    @allure.title('Checking the opening of the ingredient pop-up window')
    @allure.description('Checks that clicking on the ingredient opens pop-up window with the ingredient info')
    def test_click_on_ingredient_opens_popup_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_fluoric_bun()
        assert main_page.check_open_details(), \
            'Unable to open ingredient pop-up window'

    @allure.title('Checking the closing of the ingredient pop-up window')
    @allure.description('Checks that clicking on the close button of the ingredient pop-up window closes the window')
    def test_click_on_ingredient_details_window_close_button_closes_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_fluoric_bun()
        main_page.close_details()
        assert not main_page.check_absent_button(), \
            'Unable to close ingredient pop-up window'

    @allure.title('Checking increasing of the ingredient counter')
    @allure.description('Checks that adding ingredient to the order increases its counter by certain amount')
    @pytest.mark.parametrize('counter_locator, counter_step, description', CommonData.ingredients)
    def test_increase_of_ingredient_counter(self, driver, counter_locator, counter_step, description):
        main_page = MainPage(driver)
        initial_counter = int(main_page.get_text_element(counter_locator))
        main_page.drag_and_drop_element(counter_locator, Mpl.constructor_upper_bun_placeholder)
        final_counter = int(main_page.get_text_element(counter_locator))
        assert (final_counter - initial_counter) == counter_step, \
            f'The {description} counter did not increase by {counter_step} after adding {description} to the order'

    @allure.title('Checking that authorised user is able to make an order')
    @allure.description('Checks that authorised user is able to make compile a burger and place an order')
    def test_authorised_user_place_order(self, driver, create_user, sign_in):
        main_page = MainPage(driver)
        main_page.create_new_order()
        assert main_page.check_order_history(), 'Unable to place an order'