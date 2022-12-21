from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium import webdriver
import time
import unittest
import sys
sys.path.append(".")


class  TestChangePassword(unittest.TestCase):
    def __init__(
            self,
            config,
            input_text: str = None,
            need_check_output: bool = True,
            web_login_func=None,
            post_url: str = None,
            **kwargs,
    ):
        if not hasattr(self, "general_test"):
            raise AttributeError("general_test not implemented")
        super().__init__("general_test")

        self.config = config
        self.input_text = input_text
        self.need_check_output = need_check_output
        self.web_login_func = web_login_func
        self.post_url = post_url

    def setUp(self):
        self.driver = webdriver.Chrome(self.config.driver_path)
        self.driver.get(self.post_url)
        self.web_login_func(self.driver)

    def tearDown(self):
        self.driver.quit()

    def _base_step(self, text: str = None):
        time.sleep(10)
        # usecase_1: test_changepassIncorrectCurrentPassword
        self.driver.find_element(By.CSS_SELECTOR, ".toggle-icon").click()
        self.driver.find_element(By.LINK_TEXT, "Thay đổi mật khẩu").click()
        self.driver.find_element(By.ID, "ctrl_password_original").send_keys("413431\`")
        self.driver.find_element(By.ID, "ctrl_password").send_keys("1812293")
        self.driver.find_element(By.ID, "ctrl_password_confirm").send_keys("1812293")
        self.driver.find_element(By.NAME, "save").click()
        # wait 5s and reload page tinhte.vn
        time.sleep(5)
        self.driver.get("https://tinhte.vn/")
        time.sleep(5)

        # usecase_2: test_changepassMiss
        self.driver.find_element(By.CSS_SELECTOR, ".toggle-icon").click()
        self.driver.find_element(By.LINK_TEXT, "Thay đổi mật khẩu").click()
        self.driver.find_element(By.ID, "ctrl_password_original").click()
        self.driver.find_element(By.ID, "ctrl_password_original").send_keys("1813060")
        self.driver.find_element(By.ID, "ctrl_password").send_keys("43141")
        self.driver.find_element(By.ID, "ctrl_password_confirm").send_keys("43143143141")
        self.driver.find_element(By.NAME, "save").click()
        # wait 5s and reload page tinhte.vn
        time.sleep(5)
        self.driver.get("https://tinhte.vn/")
        time.sleep(5)
        #usecase_3: test_changepassNoCurrentPassword
        self.driver.find_element(By.CSS_SELECTOR, ".toggle-icon").click()
        self.driver.find_element(By.LINK_TEXT, "Thay đổi mật khẩu").click()
        self.driver.find_element(By.ID, "ctrl_password").send_keys("1812293")
        self.driver.find_element(By.ID, "ctrl_password_confirm").send_keys("1812293")
        self.driver.find_element(By.NAME, "save").click()
        # wait 5s and reload page tinhte.vn
        time.sleep(5)
        self.driver.get("https://tinhte.vn/")
        time.sleep(5) 

        #usecase_4: test_changepassNoInput
        self.driver.find_element(By.CSS_SELECTOR, ".toggle-icon").click()
        self.driver.find_element(By.LINK_TEXT, "Thay đổi mật khẩu").click()
        self.driver.find_element(By.NAME, "save").click()
        # wait 5s and reload page tinhte.vn
        time.sleep(5)
        self.driver.get("https://tinhte.vn/")
        time.sleep(5)
        #usecase_5: test_changepassNoNewPassword
        element = self.driver.find_element(By.CSS_SELECTOR, ".jsx-306557543 > .jsx-306557543")
        self.driver.find_element(By.CSS_SELECTOR, ".toggle-icon").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".toggle-icon")
        self.driver.find_element(By.LINK_TEXT, "Thay đổi mật khẩu").click()
        self.driver.find_element(By.ID, "ctrl_password_original").send_keys("1813060")
        self.driver.find_element(By.ID, "ctrl_password_confirm").send_keys("1812293")
        self.driver.find_element(By.NAME, "save").click()
        # wait 5s and reload page tinhte.vn
        time.sleep(5)
        self.driver.get("https://tinhte.vn/")
        time.sleep(5)
        #usecase_6: test_changepassNoNewPasswordAuthen
        self.driver.find_element(By.CSS_SELECTOR, ".toggle-icon").click()
        self.driver.find_element(By.LINK_TEXT, "Thay đổi mật khẩu").click()
        self.driver.find_element(By.ID, "ctrl_password_original").send_keys("1813060")
        self.driver.find_element(By.ID, "ctrl_password").send_keys("1812293")
        self.driver.find_element(By.NAME, "save").click()
        # wait 5s and reload page tinhte.vn
        time.sleep(5)
        self.driver.get("https://tinhte.vn/")
        time.sleep(5)
        
        #usecase_7: test_changepassSuccessfully
        self.driver.find_element(By.CSS_SELECTOR, ".toggle-icon").click()
        self.driver.find_element(By.LINK_TEXT, "Thay đổi mật khẩu").click()
        self.driver.find_element(By.ID, "ctrl_password_original").send_keys("1813060")
        self.driver.find_element(By.ID, "ctrl_password").send_keys("1812293")
        self.driver.find_element(By.ID, "ctrl_password_confirm").send_keys("1812293")
        self.driver.find_element(By.NAME, "save").click()
        time.sleep(5)
        self.driver.close()
  
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def _check_output(self):
        self.assertTrue(self.is_element_present(
            By.XPATH, f"//a[contains(text(),\'{self.config.web_username}\')]"))

    def general_test(self):
        self._base_step(self.input_text)
        if self.need_check_output:
            self._check_output()


if __name__ == "__main__":
    from config.config import Config

    config = Config()
    suite = unittest.TestSuite()
    suite.addTest(
         TestChangePassword(config=config, post_url="https://tinhte.vn/"))
    unittest.TextTestRunner().run(suite)

