import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class TestSearchSuite(unittest.TestCase):
    def __init__(
            self,
            config,
            testcase_name: str = None,
            input_text: str = None,
            need_check_output: bool = True,
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
        self.web_url = config.web_url

    def setUp(self):
        self.driver = webdriver.Chrome(self.driver_path)
        self.driver.get(self.web_url)
        self.vars = {}

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

    def test_searchALink(self):
        self.general_test("https://e-learning.hcmut.edu.vn/course/view.php?id=67808")

    def test_searchAStringAndNoSpaceCharacter(self):
        self.general_test("kiemtraphanmem")

    def test_searchAStringWithHieroglyphicsCharacter(self):
        self.general_test("ナム人")

    def test_searchAStringWithSpaceCharacter(self):
        self.general_test("hello hello")

    def test_searchAStringWithSpecialCharacter(self):
        self.general_test("xin#@$")

    def test_searchAStringWithUnicodeCharacter(self):
        self.general_test("xin chào")

    def test_searchWithTextHaveAnOnlyCharacter(self):
        self.general_test("a")

    def test_searchWithTextHaveOnlyOneOrMoreSpaceCharacter(self):
        self.general_test("  ")

    def test_searchWithoutACharacter(self):
        self.general_test(need_check_output=False)


if __name__ == "__main__":
    PATH = "chromedriver/chromedriver.exe"
    WEB_URL = "https://tinhte.vn/"
    suite = unittest.TestSuite()
    suite.addTest(TestSearchSuite(testcase_name="searchAStringWithUnicodeCharacter", driver_path=PATH, web_url=WEB_URL))
    unittest.TextTestRunner().run(suite)
