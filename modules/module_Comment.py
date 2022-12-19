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
            testcase_name: str = None,
            input_text: str = None,
            need_check_output: bool = True,
            web_login_func=None,
            post_url: str = None,
            **kwargs,
    ):
        testcase_name = f"test_{testcase_name}" if testcase_name else "general_test"
        if testcase_name == "general_test" and input_text is None:
            raise ValueError("Must specify input text if want use 'general_test'")
        if not hasattr(self, testcase_name):
            raise AttributeError(f"{testcase_name} not implemented")
        super().__init__(testcase_name)

        self.input_text = input_text
        self.need_check_output = need_check_output
        self.driver_path = config.path
        self.web_login_func = web_login_func
        self.post_url = post_url
        self.web_username = config.web_username

    def setUp(self):
        self.driver = webdriver.Chrome(self.driver_path)
        self.driver.get(self.post_url)
        self.web_login_func(self.driver)
        self.vars = {}

    def tearDown(self):
        self.driver.quit()

    def _base_step(self, text: str = None):
        locator = (
        By.CSS_SELECTOR, ".jsx-3593820457:nth-child(2) > .jsx-3593820457 #post-reply-63726794-x > .post-reply-input")
        wait = WebDriverWait(self.driver, 10)
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
        self.assertTrue(self.is_element_present(By.XPATH, f"//a[contains(text(),\'{self.web_username}\')]"))

    def general_test(self):
        self._base_step(self.input_text)
        if self.need_check_output:
            self._check_output()

    def test_commentBlank(self):
        self.general_test()

    def test_commentWithHieroglyphicsCharacter(self):
        self.general_test("ベトナ")

    def test_commentWithHyperlink(self):
        self.general_test("https://e-learning.hcmut.edu.vn/course/view.php?id=67808")

    def test_commentWithWhitespaceOnly(self):
        self.general_test(" ")


if __name__ == "__main__":
    PATH = "chromedriver/chromedriver.exe"
    WEB_URL = "https://tinhte.vn/"
    suite = unittest.TestSuite()
    suite.addTest(
        TestCommentSuite(testcase_name="commentWithHieroglyphicsCharacter", driver_path=PATH, web_url=WEB_URL))
    unittest.TextTestRunner().run(suite)
