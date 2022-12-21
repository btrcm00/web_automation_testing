from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import sys

sys.path.append(".")


class TestSearchSuite(unittest.TestCase):
    def __init__(
            self,
            config,
            input_text: str = None,
            **kwargs,
    ):
        super().__init__("general_test")
        self.config = config
        self.input_text = input_text
        self.data = kwargs.get("data", {})

    def setUp(self):
        self.driver = webdriver.Chrome(self.config.driver_path)
        self.driver.get(self.config.web_url)

    def tearDown(self):
        self.driver.quit()

    def _base_step(self, text: str = None):
        self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").click()
        if text is not None:
            self.driver.find_element(
                By.CSS_SELECTOR, ".search-textbox").send_keys(text)
        self.driver.find_element(
            By.CSS_SELECTOR, ".search-textbox").send_keys(Keys.ENTER)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def _check_output(self):
        not_found_ele = "//div[@id=\'content\']/div/div/div/div/div[2]/h1"
        found_ele = "//div[@id=\'content\']/div/div/div/div/div/div[2]/h1"
        return self.is_element_present(By.XPATH, not_found_ele) or self.is_element_present(By.XPATH, found_ele)

    def general_test(self):
        self._base_step(self.input_text)
        output = self._check_output()
        self.data["output"] = "PASSED" if output else "FAILED"
        self.assertTrue(output)


if __name__ == "__main__":
    from config.config import Config
    config = Config()
    suite = unittest.TestSuite()
    suite.addTest(TestSearchSuite(config=config, input_text="hihi"))
    unittest.TextTestRunner().run(suite)
