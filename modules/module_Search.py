from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config.config import *

class TestDefaultSuite:
  def setup_method(self, method):
    self.driver = webdriver.Chrome(PATH)
    self.driver.get(WEB_URL)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_searchALink(self):
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").click()
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys("https://e-learning.hcmut.edu.vn/course/view.php?id=67808")
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys(Keys.ENTER)

  def test_searchAStringAndNoSpaceCharacter(self):
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").click()
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys("kiemtraphanmem")
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys(Keys.ENTER)

  def test_searchAStringWithHieroglyphicsCharacter(self):
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").click()
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys("ナム人")
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys(Keys.ENTER)

  def test_searchAStringWithSpaceCharacter(self):
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").click()
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys("hello hello")
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys(Keys.ENTER)

  def test_searchAStringWithSpecialCharacter(self):
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").click()
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys("xin#@$")
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys(Keys.ENTER)

  def test_searchAStringWithUnicodeCharacter(self):
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").click()
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys("xin chào")
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys(Keys.ENTER)

  def test_searchWithTextHaveAnOnlyCharacter(self):
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").click()
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys("a")
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys(Keys.ENTER)

  def test_searchWithTextHaveOnlyOneOrMoreSpaceCharacter(self):
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").click()
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys("  ")
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".baseHtml > .OverlayCloser").click()

  def test_searchWithoutACharacter(self):
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").click()
    self.driver.find_element(By.CSS_SELECTOR, ".search-textbox").send_keys(Keys.ENTER)
