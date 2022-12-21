from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium import webdriver
import time
import unittest
import sys
sys.path.append(".")

class TestSendMassage(unittest.TestCase):
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
        time.sleep(5)
        #usecase_1: test_messageFullComplete
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-203918857:nth-child(2) .jsx-2504361010 > .jsx-4205696072").click()
        self.driver.find_element(By.LINK_TEXT, "Xem tất cả").click()
        self.driver.find_element(By.CSS_SELECTOR, ".topCtrl span").click()
        self.driver.find_element(By.ID, "ctrl_recipients").click()
        self.driver.find_element(By.ID, "ctrl_recipients").send_keys("hoangthh1612, ")
        self.driver.find_element(By.ID, "ctrl_title").click()
        self.driver.find_element(By.ID, "ctrl_title").send_keys("Project_03")
        self.driver.switch_to.frame(0)
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>fdafda fdafda l fdajfldaf</p>'}", element)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".ctrlUnit:nth-child(3) .primary").click()
        self.driver.execute_script("window.scrollTo(0,100)")
        # wait 5s and reload page tinhte.vn
        time.sleep(5)
        self.driver.get("https://tinhte.vn/")
        time.sleep(5)
        #usecase_2: test_messageWithUnValidTitle
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-4205696072 > path:nth-child(2)").click()
        self.driver.find_element(By.LINK_TEXT, "Xem tất cả").click()
        self.driver.find_element(By.CSS_SELECTOR, ".topCtrl span").click()
        self.driver.find_element(By.ID, "ctrl_recipients").click()
        self.driver.find_element(By.ID, "ctrl_recipients").send_keys("hoangthh1612, ")
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, "p").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>fdasfdaf dsfasfdas fdsafdas&nbsp;</p>'}", element)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".ctrlUnit:nth-child(3) .primary").click()
        # wait 5s and reload page tinhte.vn
        time.sleep(5)
        self.driver.get("https://tinhte.vn/")
        time.sleep(5)
        #usecase_3: test_messageWithUnvalidPar
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-4205696072 > path:nth-child(2)").click()
        self.driver.find_element(By.LINK_TEXT, "Xem tất cả").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".topCtrl span")
        self.driver.find_element(By.CSS_SELECTOR, ".topCtrl span").click()
        self.driver.find_element(By.ID, "ctrl_recipients").click()
        self.driver.find_element(By.ID, "ctrl_recipients").send_keys("fdafdsa")
        self.driver.find_element(By.ID, "ctrl_title").send_keys("Project_3")
        self.driver.switch_to.frame(0)
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>fdasfda fdafdsa fdafda&nbsp;</p>'}", element)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".ctrlUnit:nth-child(3) .primary").click()
        # wait 5s and reload page tinhte.vn
        time.sleep(5)
        self.driver.get("https://tinhte.vn/")
        time.sleep(5) 

        #usecase_4: test_messageWithoutMess
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-4205696072 > path:nth-child(2)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".jsx-4205696072 > path:nth-child(2)")      
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        self.driver.find_element(By.LINK_TEXT, "Xem tất cả").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".topCtrl span")
        self.driver.find_element(By.CSS_SELECTOR, ".topCtrl span").click()
        self.driver.find_element(By.ID, "ctrl_recipients").click()
        self.driver.find_element(By.ID, "ctrl_recipients").send_keys("hoangthh1612, ")
        self.driver.find_element(By.ID, "ctrl_title").send_keys("Project_03")
        self.driver.find_element(By.CSS_SELECTOR, ".ctrlUnit:nth-child(3) .primary").click()
        # wait 5s and reload page tinhte.vn
        time.sleep(5)
        self.driver.get("https://tinhte.vn/")
        time.sleep(5)
        #usecase_5: test_messageWithoutPar
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-4205696072 > path:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".jsx-4205696072 > path:nth-child(1)")
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        self.driver.find_element(By.LINK_TEXT, "Xem tất cả").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".topCtrl span")
        self.driver.find_element(By.CSS_SELECTOR, ".topCtrl span").click()
        self.driver.find_element(By.ID, "ctrl_title").click()
        self.driver.find_element(By.ID, "ctrl_title").send_keys("Project_3")
        self.driver.switch_to.frame(0)
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>fdasf fdsafda fdafa fdafda&nbsp;</p>'}", element)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".ctrlUnit:nth-child(3) .primary").click()
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
        TestSendMassage(config=config, post_url="https://tinhte.vn/"))
    unittest.TextTestRunner().run(suite)

