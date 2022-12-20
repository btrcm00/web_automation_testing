import sys
sys.path.append(".")

import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCommentSuite(unittest.TestCase):
    def __init__(
            self,
            config,
            input_text: str = None,
            web_login_func=None,
            post_url: str = None,
            **kwargs,
    ):
        if not hasattr(self, "general_test"):
            raise AttributeError("general_test not implemented")
        super().__init__("general_test")

        self.config = config
        self.input_text = input_text
        self.web_login_func = web_login_func
        self.post_url = post_url

    def setUp(self):
        self.driver = webdriver.Chrome(self.config.driver_path)
        self.driver.get(self.post_url)
        self.web_login_func(self.driver)

    def tearDown(self):
        self.driver.quit()

    def _base_step(self, text: str = None):
        locator = (
            By.CSS_SELECTOR,
            ".jsx-3593820457:nth-child(2) > .jsx-3593820457 #post-reply-63726794-x > .post-reply-input")
        wait = WebDriverWait(self.driver, self.config.locator_wait_time)
        wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.find_element(*locator).click()
        if text is not None:
            self.driver.find_element(*locator).send_keys(text)
        self.driver.find_element(By.CSS_SELECTOR, ".active:nth-child(3)").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def _check_output(self):
        output = self.is_element_present(By.XPATH, f"//a[contains(text(),\'{self.config.web_username}\')]")
        return "PASSED" if output else "FAILED"

    def general_test(self):
        self._base_step(self.input_text)
        return self._check_output()
            

if __name__ == "__main__":
    from config.config import Config

    config = Config()
    suite = unittest.TestSuite()
    suite.addTest(
        TestCommentSuite(config=config, post_url="https://tinhte.vn/thread/elon-musk-hoi-y-kien-nguoi-dung-ve-viec-co-nen-tu-chuc-ceo-cua-twitter-hay-khong.3611655"))
    unittest.TextTestRunner().run(suite)
