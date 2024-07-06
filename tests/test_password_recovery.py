import allure
from data import Urls

from pages.forgot_password_page import ForgotPasswordPage
from pages.main_page import MainPage



class TestPasswordRecovery:

    @allure.title('Checking the transition to the "Forgot Password" page')
    @allure.description('Checks that clicking on the "Recover Password" button opens "Forgot Password" page')
    def test_click_on_pass_recovery_button_opens_pass_recovery_page(self, driver, get_forgot_pass_page):
        forgot_pass_page = ForgotPasswordPage(driver)
        assert forgot_pass_page.get_current_page_url() == Urls.forgot_password_url, \
            'Unable to get Forgot Password page'

    @allure.title('Checking the transition to the "Reset password" page')
    @allure.description('Checks that entering email and clicking on the "Recover Password" button'
                        ' opens "Reset Password" page')
    def test_input_email_and_click_on_pass_recovery_button_opens_reset_pass_page(self, driver, get_forgot_pass_page):
        forgot_pass_page = ForgotPasswordPage(driver)
        forgot_pass_page.send_user_email_and_click_recover()
        reset_pass_page = MainPage(driver)
        assert reset_pass_page.check_password_page(), 'Unable to get Reset Password page'

    @allure.title('Checking the focus on Password entry field')
    @allure.description('Checks that clicking on the "Show/Hide Password" button'
                        ' highlights the Password entry field on "Reset Password" page')
    def test_highlight_pass_entry_field(self, driver, get_forgot_pass_page):
        forgot_pass_page = ForgotPasswordPage(driver)
        forgot_pass_page.send_user_email_and_click_recover()
        reset_pass_page = MainPage(driver)
        reset_pass_page.show_password()
        assert reset_pass_page.check_highlight_password(), \
            'Password entry field on "Reset Password" page is not highlighted'

