import allure
from data import Urls

from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestAccount:

    @allure.title('Checking the transition to the "Profile" page')
    @allure.description('Checks that clicking on the "Account" button in the header opens "Profile" page.')
    def test_click_on_account_button_opens_profile_page(self, driver, create_user, sign_in):
        main_page = MainPage(driver)
        main_page.click_on_account_button()
        profile_page = ProfilePage(driver)
        assert profile_page.check_profile_url(), 'Unable to get Profile page'

    @allure.title('Checking the transition to the "Orders History" ')
    @allure.description('Checks that clicking on the "Orders History" url in the Profile opens "Orders History".')
    def test_click_on_order_history_url_opens_orders_history_page(self, driver, create_user, sign_in):
        main_page = MainPage(driver)
        main_page.click_on_account_button()
        profile_page = ProfilePage(driver)
        profile_page.click_on_order_history()
        assert profile_page.get_current_page_url() == Urls.order_history_url, 'Unable to get Order History page'

    @allure.title('Checking the exit from account ')
    @allure.description('Checks that clicking on the "Exit" button in the Profile leads to logout')
    def test_click_on_exit_url_logs_out_from_account(self, driver, create_user, sign_in):
        main_page = MainPage(driver)
        main_page.click_on_account_button()
        profile_page = ProfilePage(driver)
        profile_page.click_on_exit_button()
        login_page = ProfilePage(driver)
        assert login_page.check_email_field()

