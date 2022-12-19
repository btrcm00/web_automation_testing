from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config.config import *


class TestProfileSuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(WEB_URL)
        self.vars = {}
  
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
      self.driver.find_element(By.ID, "ctrl_avatar").send_keys("\materials\random.txt")
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
    
