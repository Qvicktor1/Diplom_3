from locators.locators import FeedPageLocators as Fpl
from locators.locators import MainPageLocators as Mpl


class Urls:
    main_url = 'https://stellarburgers.nomoreparties.site/'
    forgot_password_url = 'https://stellarburgers.nomoreparties.site/forgot-password'
    order_history_url = 'https://stellarburgers.nomoreparties.site/account/order-history'
    login_url = 'https://stellarburgers.nomoreparties.site/login'
    register_url = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    delete_user_url = 'https://stellarburgers.nomoreparties.site/api/auth/user'


class CommonData:
    test_email = 'test_email@ya.ru'
    test_user_password = 'YouShallNotPass'
    test_user_name = 'Gandalf'
    counters = [
        [Fpl.completed_all_time_counter, 'Completed for all time'],
        [Fpl.completed_today_counter, 'Completed today']
    ]
    headers = [
        [Mpl.constructor_button_header, Mpl.compile_burger_header, 'Constructor'],
        [Mpl.feed_button_header, Fpl.feed_header, 'Feed']
    ]
    ingredients = [
        [Mpl.fluoric_bun_counter, 2, 'bun'],
        [Mpl.ingredient_counter, 1, 'filling']
    ]