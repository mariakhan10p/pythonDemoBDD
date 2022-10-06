from pytest_bdd import given, when, scenarios, then, parsers
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

scenarios('../features')


@given("Open Browser", scope="session")
def browser():
    """Set the capabilities and initialize the driver."""
    browser.driver = webdriver.Chrome("../../../drivers/chromedriver.exe")
    browser.driver.get("http://automationpractice.com/")
    yield browser
    browser.driver.quit()


@when("Click Women")
def click_women(browser):
    selector_women_btn = "a[title=Women]"
    print(browser.driver.title)
    element = browser.driver.find_element(By.CSS_SELECTOR, selector_women_btn)
    element.click()


@then(parsers.parse('Check page title is "{title}"'))
def check_page_title(browser, title):
    assert title in browser.driver.title
