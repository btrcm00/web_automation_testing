import sys

sys.path.append(".")

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class TestSearchSuite(unittest.TestCase):
    def __init__(
            self,
            config,
            input_text: str = None,
            need_check_output: bool = True,
            **kwargs,
    ):
        super().__init__("general_test")
        self.config = config
        self.input_text = input_text
        self.need_check_output = need_check_output
        if self.input_text is None:
            self.need_check_output = False

    def setUp(self):
        self.driver = webdriver.Chrome(self.config.driver_path)
        self.driver.get(self.config.web_url)

    def tearDown(self):
        self.driver.quit()

    def _base_step(self, text: str = None):
        self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").click()
        if text is not None:
            self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys(text)
        self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys(Keys.ENTER)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def _check_output(self):
        not_found_ele = "//div[@id=\'content\']/div/div/div/div/div[2]/h1"
        found_ele = "//div[@id=\'content\']/div/div/div/div/div/div[2]/h1"
        self.assertTrue(self.is_element_present(By.XPATH, not_found_ele) or \
                        self.is_element_present(By.XPATH, found_ele))

    def general_test(self):
        self._base_step(self.input_text)
        if self.need_check_output:
            self._check_output()


if __name__ == "__main__":
    from config.config import Config
    config = Config()
    suite = unittest.TestSuite()
    suite.addTest(TestSearchSuite(config=config))
    unittest.TextTestRunner().run(suite)
