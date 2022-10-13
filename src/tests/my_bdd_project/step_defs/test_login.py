from pytest_bdd import given, when, scenarios, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.common_utils.resource_manager import *

scenarios('../features')

locators_list = {'XPATH': By.XPATH,
                 'ID': By.ID,
                 'NAME': By.NAME,
                 'CSS': By.CSS_SELECTOR
                 }


@given("Open Browser", scope="session")
def browser():
    """Set the capabilities and initialize the driver."""
    browser.driver = webdriver.Chrome("../../../drivers/chromedriver.exe")
    browser.driver.get("http://automationpractice.com/")
    yield browser
    browser.driver.quit()


@when(parsers.parse('Click "{element}" in "{page}" by "{locator}"'))
def click_women(browser,element, page, locator):
    resource = ResourceManager(ResourceManager.get_resource_path(page))
    selector = resource.get_resource(element)
    # selector_women_btn = "a[title=Women]"
    print(browser.driver.title)
    # element = browser.driver.find_element(By.CSS_SELECTOR, selector_women_btn)
    element = browser.driver.find_element(locators_list[locator], selector)
    element.click()


@then(parsers.parse('Check page title is "{title}"'))
def check_page_title(browser, title):
    assert title in browser.driver.title
