import time

import pytest
import requests
import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data import Urls, CommonData

from pages.main_page import MainPage
from pages.login_page import LoginPage

from locators.locators import MainPageLocators as Mpl
from locators.locators import LoginPageLocators as Lpl


@pytest.fixture(params=['chrome'])
def driver(request):
    if request.param == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--ash-no-nudges")
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")
    ##driver.set_window_size(1920, 1080)
    driver.get(Urls.main_url)

    yield driver
    driver.quit()


@pytest.fixture()
def get_forgot_pass_page(driver):
    main_page = MainPage(driver)
    main_page.click_element(Mpl.account_button_header)
    login_page = LoginPage(driver)
    login_page.scroll_and_click(Lpl.forgot_password_button_login)


@pytest.fixture()
def create_user(driver):
    letters = string.ascii_lowercase
    login = ''.join(random.choice(letters) for _ in range(10)) + '@ya.ru'
    payload = {"email": f'{login}',
               "password": CommonData.test_user_password,
               "name": CommonData.test_user_name
               }
    response = requests.post(Urls.register_url, data=payload)
    access_token = response.json().get("accessToken")
    yield login
    headers = {'Authorization': f'{access_token}'}
    requests.delete(Urls.delete_user_url, headers=headers)


@pytest.fixture()
def sign_in(driver, create_user):
    login = create_user
    main_page = MainPage(driver)
    main_page.click_element(Mpl.account_button_header)
    login_page = LoginPage(driver)
    login_page.send_user_data(Lpl.email_input_field, login)
    login_page.send_user_data(Lpl.password_input_field, CommonData.test_user_password)
    login_page.click_element(Lpl.sign_in_button)
    yield


@pytest.fixture()
def create_new_order_and_get_its_number(driver):
    main_page = MainPage(driver)
    main_page.click_element(Mpl.constructor_button_header)
    main_page.drag_and_drop_element(Mpl.ingredient_name, Mpl.constructor_upper_bun_placeholder)
    main_page.drag_and_drop_element(Mpl.fluoric_bun_name, Mpl.constructor_upper_bun_placeholder)
    main_page.click_element(Mpl.place_order_button)
    time.sleep(2)
    ##main_page.check_if_created_order_number_is_shown()
    order_number = main_page.get_text_element(Mpl.order_number)
    main_page.click_element(Mpl.order_number_window_close_button)
    return order_number