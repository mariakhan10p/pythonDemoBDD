from selenium.webdriver.common.by import By


class SearchPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    SEARCH_BAR = (By.NAME, 'search_query')
    SEARCH_BTN = (By.NAME, "submit_search")


class MainPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""
    WOMEN_BTN = (By.CSS_SELECTOR, "a[title=Women]")
    CART = (By.CSS_SELECTOR, "div[class=shopping_cart] > a")
