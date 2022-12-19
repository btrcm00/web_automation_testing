import unittest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from config.config import *


class TestWebModules:
    def __init__(
            self,
            test_module: str = None,
            config: Config = None,
    ):
        self.config = config
        self.web_driver_path = config.path
        self.web_url = config.web_url
        self.web_username = config.web_username
        self.web_password = config.web_password

        if test_module is None or test_module not in MAP_MODULE_NAME_TO_CLASS.keys():
            raise "test_module must be specified"

        self.module_class = MAP_MODULE_NAME_TO_CLASS[test_module]
        self.required_params = REQUIRED_PARAM_OF_MUDULE.get(test_module, [])

    def web_login(self, driver):
        driver.find_element(By.CSS_SELECTOR, ".jsx-3867722346 > svg").click()
        driver.find_element(By.LINK_TEXT, "Đăng nhập tài khoản").click()
        driver.find_element(By.ID, "ctrl_pageLogin_login2").send_keys(self.web_username)
        driver.find_element(By.ID, "ctrl_pageLogin_password2").send_keys(self.web_password)
        driver.find_element(By.ID, "ctrl_pageLogin_password2").send_keys(Keys.ENTER)

    def test_func(self, input_data: dict):
        if any(param not in input_data.keys() for param in self.required_params):
            raise "NEED PASS ENOUGH PARAM!!!"
        suite = unittest.TestSuite()
        suite.addTest(self.module_class(config=config,
                                        web_login_func=self.web_login,
                                        **input_data))
        unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    # Ví dụ test module Search
    config = Config()
    t = TestWebModules(test_module="comment", config=config)
    t.test_func(input_data={"input_text": "bài viết bổ ích", "need_check_output": True,
                            "post_url": "https://tinhte.vn/thread/elon-musk-hoi-y-kien-nguoi-dung-ve-viec-co-nen-tu-chuc-ceo-cua-twitter-hay-khong.3611655"})
