from locators import MainPageLocators, SearchPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class SearchTextElement(BasePage):
    """This class gets the search text from the specified locator"""

    # The locator for search box where search string is entered
    def set_search_value(self, value):
        element = self.driver.find_element(*SearchPageLocators.SEARCH_BAR)
        element.clear()
        element.send_keys(value)
        return element

    def click_submit_search(self):
        element = self.driver.find_element(*SearchPageLocators.SEARCH_BTN)
        element.click


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    # Declares a variable that will contain the retrieved text

    def is_text_matches(self, text):
        element = self.driver.find_element(*MainPageLocators.WOMEN_BTN)
        return text in element.text

    def is_url_matches(self, url):
        return url in self.driver.current_url

    def is_title_matches(self, title):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return title in self.driver.title

    def click_women_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.WOMEN_BTN)
        element.click()

    def check_element(self):
        element = self.driver.find_element(*MainPageLocators.WOMEN_BTN)
        element.is_displayed()

