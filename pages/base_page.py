import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from locators.locators import MainPageLocators as Mpl

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Checking visibility of the specified element ')
    def check_element_is_visible(self, locator):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(locator))

    @allure.step('Clicking on the specified element')
    def click_element(self, locator):
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(locator)).click()




    @allure.step('Filling the specified entry field with certain data')
    def send_user_data(self, locator, data):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(data)

    @allure.step('Returning text of the specified element')
    def get_text_element(self, locator):
        return WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(locator)).text

    @allure.step('Scrolling to the specified element')
    def go_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Returning url of the current page')
    def get_current_page_url(self):
        return self.driver.current_url

    @allure.step('Scrolling to element and clicking')
    def scroll_and_click(self, locator):
        self.go_to_element(locator)
        self.click_element(locator)

    @allure.step('Checking that element is invisible')
    def check_element_is_absent(self, locator):
        WebDriverWait(self.driver, 30).until(ec.invisibility_of_element_located(locator))

    @allure.step('Checking that in certain element its text has changed')
    def wait_till_text_is_shown(self, locator, text):
        WebDriverWait(self.driver, 10).until(ec.text_to_be_present_in_element_value(locator, text))

    @allure.step('Drag and drop the element')
    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.check_element_is_visible(source_locator)
        target_element = self.check_element_is_visible(target_locator)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(source_element, target_element).perform()

    @allure.step('Clicking on account')
    def click_on_account_button(self):
        self.click_element(Mpl.account_button_header)

    @allure.step('Clicking on feed')
    def click_on_feed_button(self):
        self.click_element(Mpl.feed_button_header)
