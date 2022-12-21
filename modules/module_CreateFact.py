import sys
sys.path.append(".")
import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains


class TestCreateFactSuite(unittest.TestCase):
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

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)


        # self.driver = webdriver.Chrome(self.config.driver_path)
        self.driver.get(self.post_url)
        self.web_login_func(self.driver)

    def tearDown(self):
        self.driver.quit()
    
    def _base_step(self, text: str = None):     
        time.sleep(10)
        self.test_cFT1()
        time.sleep(3)
        self.test_cFT2()
        time.sleep(3)
        self.test_cFT3()
        time.sleep(3)
        #self.test_cFT4()
        time.sleep(3)
        self.test_cFT5()
        time.sleep(3)
        self.test_cFT6()
        time.sleep(3)
        self.test_cFT7()
        time.sleep(3)
        self.test_cST1()
        time.sleep(3)
        self.test_cST2()
        time.sleep(3)
        self.test_cST3()
        time.sleep(3)
        self.test_cST4()
        time.sleep(3)
        self.test_cST5()
        time.sleep(3)
        self.test_cST6()
        time.sleep(3)
        self.test_cST7()
        time.sleep(3)
        self.test_cST8()
        time.sleep(3)
        self.test_cST9()
        time.sleep(3)
        self.test_cST10()
        time.sleep(3)
        self.test_cST11()
        time.sleep(3)
    
    def test_cFT1(self):
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".middle-area").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()

    def test_cFT2(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".middle-area").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").send_keys("12345")
        #self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()
  
    def test_cFT3(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, ".file-upload-btn")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".file-upload-btn").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".box > .jsx-2798031272:nth-child(1)").send_keys("C:\\fakepath\\test.pdf")
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        # self.driver.find_element(By.CSS_SELECTOR, ".publish-btn").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()

  
    def test_cFT4(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").click()
        self.driver.find_element(By.CSS_SELECTOR, "g:nth-child(1) > path:nth-child(1)").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".box > .jsx-2798031272:nth-child(1)").send_keys("C:\\fakepath\\images.jpg")
        # self.driver.find_element(By.CSS_SELECTOR, ".publish-btn").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()

  
    def test_cFT5(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").send_keys("12345")
        self.driver.find_element(By.CSS_SELECTOR, "g:nth-child(1) > path:nth-child(1)").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".box > .jsx-2798031272:nth-child(1)").send_keys("C:\\fakepath\\images.jpg")
        #self.driver.find_element(By.CSS_SELECTOR, ".publish-btn").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()
  
    def test_cFT6(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".middle-area").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").send_keys("1234567891011")
        #self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".publish-btn").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()
  
    def test_cFT7(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").send_keys("tessssssssssssssssst anh")
        self.driver.find_element(By.CSS_SELECTOR, "g:nth-child(1) > path:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".box > .jsx-2798031272:nth-child(1)").send_keys("C:\\fakepath\\images.jpg")
        #self.driver.find_element(By.CSS_SELECTOR, ".publish-btn").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()

  
    def test_cST1(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".switch-toggle").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()

  
    def test_cST2(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".switch-toggle").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").send_keys("12345")
        # self.driver.find_element(By.CSS_SELECTOR, ".publish-btn").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()

    def test_cST3(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".switch-toggle").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").send_keys("12345")
        # self.driver.find_element(By.CSS_SELECTOR, ".publish-btn").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()
    
    def test_cST4(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".switch-toggle").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").send_keys("1234567891011")
        # self.driver.find_element(By.CSS_SELECTOR, ".publish-btn").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()
    
    
    def test_cST5(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".switch-toggle").click()
        self.driver.find_element(By.CSS_SELECTOR, ".link-sharing > .jsx-2008469963").click()
        self.driver.find_element(By.CSS_SELECTOR, ".switch-toggle").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()
    
    def test_cST6(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".switch-toggle").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-background-switch:nth-child(2) > .jsx-2008469963").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-2008469963:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".switch-toggle").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()
    
    def test_cST7(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".switch-toggle").click()
        self.driver.find_element(By.CSS_SELECTOR, ".link-sharing > .jsx-2008469963").click()
        self.driver.find_element(By.CSS_SELECTOR, ".link-input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".link-input").send_keys("https://www.google.com/search?q=%E1%BA%A3nh+totoro&sxsrf=ALiCzsYhPuNIKHDeRP1p-0GGnNRsD2pU7Q%3A1671355199649&source=hp&ei=P9ueY4urJaGY3LUPh7udsAU&iflsig=AJiK0e8AAAAAY57pT4pU2aGEEKwmCJgFTfrJRCjbNctk&oq=&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJ1AAWABgngZoAXAAeACAAQCIAQCSAQCYAQCwAQo&sclient=gws-wiz")
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").send_keys("123456777777777777")
        #self.driver.find_element(By.CSS_SELECTOR, ".publish-btn").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()
    
    def test_cST8(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".switch-toggle").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-background-switch:nth-child(2) > .jsx-2008469963").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-2008469963:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").send_keys("day la bai viet nhap")
        #self.driver.find_element(By.CSS_SELECTOR, ".publish-btn").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()
    
    def test_cST9(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".switch-toggle").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-background-switch:nth-child(2) > .jsx-2008469963").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-2008469963:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").send_keys("day la bai test9")
        #self.driver.find_element(By.CSS_SELECTOR, ".publish-btn").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()
    
    def test_cST10(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".switch-toggle").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-background-switch:nth-child(2) > .jsx-2008469963").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-2008469963:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").send_keys("day la test 10")
        #self.driver.find_element(By.CSS_SELECTOR, ".publish-btn").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()

    def test_cST11(self):
        self.driver.get("https://tinhte.vn/")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-690238688:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".switch-toggle").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-background-switch:nth-child(2) > .jsx-2008469963").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-2008469963:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-editor-textarea").send_keys("day la test 11")
        #self.driver.find_element(By.CSS_SELECTOR, ".publish-btn").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".reset-btn > svg").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def _check_output(self):
        self.assertTrue(self.is_element_present(By.XPATH, f"//a[contains(text(),\'{self.config.web_username}\')]"))

    def general_test(self):
        self._base_step(self.input_text)
        #self._base_step()
        if self.need_check_output:
            self._check_output()


if __name__ == "__main__":
    from config.config import Config

    config = Config()
    suite = unittest.TestSuite()
    suite.addTest(
        TestCreateFactSuite(config=config, post_url="https://tinhte.vn/"))
    unittest.TextTestRunner().run(suite)
