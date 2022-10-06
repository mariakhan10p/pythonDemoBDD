import unittest
from selenium import webdriver

from tests.my_tests import page


class PythonSearch(unittest.TestCase):
    url = "http://automationpractice.com/index.php"

    def setUp(self):
        self.driver = webdriver.Chrome("../../drivers/chromedriver.exe")
        self.driver.get(self.url)
        driver = self.driver
        driver.maximize_window()
        driver.set_page_load_timeout(30)

    def test_first(self):
        driver = self.driver
        main_page = page.MainPage(driver)
        search_page = page.SearchTextElement(driver)
        main_page.is_url_matches(self.url)
        main_page.is_title_matches("My Store")
        search_page.set_search_value("dress")
        search_page.click_submit_search()
        main_page.is_title_matches("Search")
        search_page.set_search_value("Maria")
        main_page.check_element()
        main_page.is_text_matches("WOMEN")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
