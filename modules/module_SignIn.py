import time
import unittest
import sys
sys.path.append(".")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestSignInSuite(unittest.TestCase):
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
  
    def teardown_method(self):
        self.driver.quit()
    
    def test_noInput(self):
        # self.driver.get("https://tinhte.vn/")
        # WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".profile-button > .avatar")))
        # self.driver.find_element(By.CSS_SELECTOR, ".profile-button > .avatar").click()
        # self.driver.find_element(By.LINK_TEXT, "Đăng xuất").click()
        # time.sleep(2)
        # self.driver.find_element(By.LINK_TEXT, "Đăng xuất").click()
        # WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".tinhte-logo")))
        self.driver.get("https://tinhte.vn/login/")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "ctrl_pageLogin_login2")))
        time.sleep(2)
        self.driver.find_element(By.ID, "ctrl_pageLogin_login2").send_keys("")
        self.driver.find_element(By.ID, "ctrl_pageLogin_password2").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(4)").click()
        self.driver.close()
    
    def test_noPassword(self):
        self.driver.get("https://tinhte.vn/login/")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "ctrl_pageLogin_login2")))
        time.sleep(2)
        self.driver.find_element(By.ID, "ctrl_pageLogin_login2").send_keys("minhbtcm00")
        self.driver.find_element(By.ID, "ctrl_pageLogin_password2").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(4)").click()
        self.driver.close()

    def test_invalidPassword(self):
        self.driver.get("https://tinhte.vn/login/")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "ctrl_pageLogin_login2")))
        time.sleep(2)
        self.driver.find_element(By.ID, "ctrl_pageLogin_login2").send_keys("minhbtcm00")
        self.driver.find_element(By.ID, "ctrl_pageLogin_password2").send_keys("123456789789")
        self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(4)").click()
        self.driver.close()
    
    def test_successfulLogin(self):
        self.driver.get("https://tinhte.vn/login/")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "ctrl_pageLogin_login2")))
        time.sleep(2)
        self.driver.find_element(By.ID, "ctrl_pageLogin_login2").send_keys("minhbtcm00")
        self.driver.find_element(By.ID, "ctrl_pageLogin_password2").send_keys("1813060")
        self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(4)").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".profile-button > .avatar")))
        self.driver.close()

if __name__ == "__main__":
    from config.config import Config

    config = Config()
    suite = unittest.TestSuite()
    suite.addTest(
        TestSignInSuite(config=config, post_url="https://tinhte.vn/"))
    unittest.TextTestRunner().run(suite)
    
