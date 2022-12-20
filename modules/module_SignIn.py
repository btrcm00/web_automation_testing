from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config.config import *


class TestSignInSuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(WEB_URL)
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_noInput(self):
        self.driver.get("https://tinhte.vn/login/")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "ctrl_pageLogin_login2")))
        time.sleep(30)
        self.driver.find_element(By.ID, "ctrl_pageLogin_login2").send_keys("")
        self.driver.find_element(By.ID, "ctrl_pageLogin_password2").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(4)").click()
        self.driver.close()
    
    def test_invalidPassword(self):
        self.driver.get("https://tinhte.vn/login/")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "ctrl_pageLogin_login2")))
        time.sleep(30)
        self.driver.find_element(By.ID, "ctrl_pageLogin_login2").send_keys("minhbtcm00")
        self.driver.find_element(By.ID, "ctrl_pageLogin_password2").send_keys("123456789789")
        self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(4)").click()
        self.driver.close()
    
    def test_successfulLogin(self):
        self.driver.get("https://tinhte.vn/login/")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "ctrl_pageLogin_login2")))
        time.sleep(30)
        self.driver.find_element(By.ID, "ctrl_pageLogin_login2").send_keys("minhbtcm00")
        self.driver.find_element(By.ID, "ctrl_pageLogin_password2").send_keys("1813060")
        self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(4)").click()
        time.sleep(30)
        self.driver.find_element(By.CSS_SELECTOR, ".profile-button > .avatar").click()
        self.driver.find_element(By.LINK_TEXT, "Đăng xuất").click()
        time.sleep(30)
        self.driver.find_element(By.LINK_TEXT, "Đăng xuất").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".tinhte-logo")))
        self.driver.close()
    
    def test_noPassword(self):
        self.driver.get("https://tinhte.vn/login/")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "ctrl_pageLogin_login2")))
        time.sleep(30)
        self.driver.find_element(By.ID, "ctrl_pageLogin_login2").send_keys("minhbtcm00")
        self.driver.find_element(By.ID, "ctrl_pageLogin_password2").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(4)").click()
        self.driver.close()
    
