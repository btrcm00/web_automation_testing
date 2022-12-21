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


class TestProfileSuite(unittest.TestCase):
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
        self.data = kwargs.get("data", {})

    def setUp(self):
        self.driver = webdriver.Chrome(self.config.driver_path)
        self.driver.get(self.post_url)
        self.web_login_func(self.driver)
  
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_changeAvatar(self):
      self.driver.get("https://tinhte.vn/account/personal-details")
      self.driver.find_element(By.CSS_SELECTOR, ".OverlayTrigger > .img").click()
      self.driver.find_element(By.ID, "ctrl_avatar").click()
      self.driver.find_element(By.ID, "ctrl_avatar").send_keys("\materials\logo.png")
      self.driver.find_element(By.ID, "ctrl_save").click()
      self.driver.close()
    
    def test_changeAvatarWithWrongType(self):
      self.driver.get("https://tinhte.vn/account/personal-details")
      self.driver.find_element(By.CSS_SELECTOR, ".OverlayTrigger > .img").click()
      self.driver.find_element(By.ID, "ctrl_avatar").click()
      self.driver.find_element(By.ID, "ctrl_avatar").send_keys("\materials\sample.txt")
      self.driver.find_element(By.CSS_SELECTOR, ".baseHtml").click()
      self.driver.find_element(By.CSS_SELECTOR, ".OverlayCloser:nth-child(1)").click()
      self.driver.close()
    
    def test_invalidHomePage(self):
      self.driver.get("https://tinhte.vn/account/personal-details")
      self.driver.find_element(By.ID, "ctrl_homepage").click()
      self.driver.find_element(By.ID, "ctrl_homepage").send_keys("youtube")
      self.driver.find_element(By.NAME, "save").click()
      self.driver.close()
    
    def test_invalidPhoneNumber(self):
      self.driver.get("https://tinhte.vn/account/personal-details")
      self.driver.find_element(By.ID, "ctrl_custom_field_citizenPhoneNumber").click()
      self.driver.find_element(By.ID, "ctrl_custom_field_citizenPhoneNumber").send_keys("038asd1234")
      self.driver.find_element(By.NAME, "save").click()
      self.driver.find_element(By.CSS_SELECTOR, ".errorOverlay > .close").click()
      self.driver.close()
    
    def test_noAddress(self):
      self.driver.get("https://tinhte.vn/account/personal-details")
      self.driver.find_element(By.ID, "ctrl_location").click()
      self.driver.find_element(By.ID, "ctrl_location").send_keys("")
      self.driver.find_element(By.NAME, "save").click()
      self.driver.close()
    
    def test_noHomePage(self):
      self.driver.get("https://tinhte.vn/account/personal-details")
      self.driver.find_element(By.ID, "ctrl_homepage").send_keys("")
      self.driver.find_element(By.NAME, "save").click()
      self.driver.close()
    
    def test_noPhoneNumber(self):
      self.driver.get("https://tinhte.vn/account/personal-details")
      self.driver.find_element(By.ID, "ctrl_custom_field_citizenPhoneNumber").send_keys("")
      self.driver.find_element(By.NAME, "save").click()
      self.driver.close()
    
    def test_updateAddressWithUnicode(self):
      self.driver.get("https://tinhte.vn/account/personal-details")
      self.driver.find_element(By.ID, "ctrl_location").click()
      self.driver.find_element(By.ID, "ctrl_location").send_keys("ベトナムの都市")
      self.driver.find_element(By.ID, "ctrl_location").send_keys(Keys.ENTER)
      self.driver.find_element(By.NAME, "save").click()
      self.driver.close()
    
    def test_updateAddress(self):
      self.driver.get("https://tinhte.vn/account/personal-details")
      self.driver.find_element(By.ID, "ctrl_location").click()
      self.driver.find_element(By.ID, "ctrl_location").send_keys("123 Cộng Hoà, quận Tân Bình, TPHCM")
      self.driver.find_element(By.ID, "ctrl_location").send_keys(Keys.ENTER)
      self.driver.find_element(By.NAME, "save").click()
      self.driver.close()
    
    def test_updateHomePage(self):
      self.driver.get("https://tinhte.vn/account/personal-details")
      self.driver.find_element(By.ID, "ctrl_homepage").click()
      self.driver.find_element(By.ID, "ctrl_homepage").send_keys("https://www.youtube.com/")
      self.driver.find_element(By.NAME, "save").click()
      self.driver.close()
    
    def test_updatePhoneNumber(self):
      self.driver.get("https://tinhte.vn/account/personal-details")
      self.driver.find_element(By.ID, "ctrl_custom_field_citizenPhoneNumber").click()
      self.driver.find_element(By.ID, "ctrl_custom_field_citizenPhoneNumber").send_keys("0386083201")
      self.driver.find_element(By.NAME, "save").click()
      self.driver.close()
    
if __name__ == "__main__":
    PATH = "chromedriver/chromedriver.exe"
    WEB_URL = "https://tinhte.vn/"
    suite = unittest.TestSuite()
    suite.addTest(TestProfileSuite(testcase_name="changeAvatar", driver_path=PATH, web_url=WEB_URL))
    unittest.TextTestRunner().run(suite)