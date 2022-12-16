from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config.config import *


class TestSearchSuite:
    def setup_method(self, method):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(WEB_URL)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def _base_search_step(self, text: str = None):
        self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").click()
        if text is not None:
            self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys(text)
        self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys(Keys.ENTER)

    def test_searchALink(self):
        self._base_search_step("https://e-learning.hcmut.edu.vn/course/view.php?id=67808")

    def test_searchAStringAndNoSpaceCharacter(self):
        self._base_search_step("kiemtraphanmem")

    def test_searchAStringWithHieroglyphicsCharacter(self):
        self._base_search_step("ナム人")

    def test_searchAStringWithSpaceCharacter(self):
        self._base_search_step("hello hello")

    def test_searchAStringWithSpecialCharacter(self):
        self._base_search_step("xin#@$")

    def test_searchAStringWithUnicodeCharacter(self):
        self._base_search_step("xin chào")

    def test_searchWithTextHaveAnOnlyCharacter(self):
        self._base_search_step("a")

    def test_searchWithTextHaveOnlyOneOrMoreSpaceCharacter(self):
        self._base_search_step("  ")

    def test_searchWithoutACharacter(self):
        self._base_search_step()
