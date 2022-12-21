import os.path
import unittest
from typing import Dict
import pandas as pd

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from config.common import *
from config.config import *


class TestWebModules:
    def __init__(
            self,
            module_name: str = None,
            config: Config = None,
            extra_data: dict = None
    ):
        self.config = config
        self.module_name = module_name
        if module_name is None or module_name not in MAP_MODULE_NAME_TO_CLASS.keys():
            raise "test_module must be specified"

        self.module_class = MAP_MODULE_NAME_TO_CLASS[module_name]
        self.required_params = REQUIRED_PARAM_OF_MUDULE.get(module_name, [])
        self.sheet_params = PARAMS_OF_MODULE_IN_SHEET.get(module_name)
        self.extra_data = extra_data if extra_data is not None else {}

    def web_login(self, driver: WebDriver):
        driver.find_element(By.CSS_SELECTOR, ".jsx-3867722346 > svg").click()
        driver.find_element(By.LINK_TEXT, "Đăng nhập tài khoản").click()
        driver.find_element(By.ID, "ctrl_pageLogin_login2").send_keys(self.config.web_username)
        driver.find_element(By.ID, "ctrl_pageLogin_password2").send_keys(self.config.web_password)
        driver.find_element(By.ID, "ctrl_pageLogin_password2").send_keys(Keys.ENTER)

    def test_func(self, data: Dict):
        # if any(param not in data.keys() for param in self.required_params):
        #     raise "NEED PASS ENOUGH PARAM!!!"
        suite = unittest.TestSuite()
        suite.addTest(self.module_class(config=config,
                                        web_login_func=self.web_login,
                                        data=data,
                                        **data))
        unittest.TextTestRunner().run(suite)

    def load_data(self, file_name):
        data_file_path = f"{self.config.input_data_folder}/{file_name}"
        if not os.path.isfile(data_file_path):
            raise "FILE NOT FOUND"
        data = pd.read_excel(data_file_path, sheet_name=self.module_name, index_col=0)
        return data

    def save_data(self, data, file_name: str):
        data_file_path = f"{self.config.output_data_folder}/{file_name}"
        data_ = pd.DataFrame().from_dict(data)
        if not os.path.isfile(data_file_path):
            data_.to_excel(data_file_path, sheet_name=self.module_name, index=False)
            return
        with pd.ExcelWriter(data_file_path, engine='openpyxl', mode='a') as writer:
            data_.to_excel(writer, sheet_name=self.module_name, index=False)

    def run_script_with_testdata(self, data_file_name: str):
        test_data = self.load_data(data_file_name)
        output_data = {
            col: list(test_data[col].values) for col in test_data.columns
        }
        for idx in range(1, test_data.shape[0]):
            input_data = {**test_data.iloc[idx][self.sheet_params], **self.extra_data}
            self.test_func(data=input_data)
            output_data["output"][idx] = input_data["output"]
        self.save_data(output_data, data_file_name)


if __name__ == "__main__":
    config = Config()
    extra_data = {
        "post_url": "https://tinhte.vn/thread/elon-musk-hoi-y-kien-nguoi-dung-ve-viec-co-nen-tu-chuc-ceo-cua-twitter-hay-khong.3611655"}
    # t = TestWebModules(module_name="comment", config=config, extra_data=extra_data)
    t = TestWebModules(module_name="search", config=config)
    t.run_script_with_testdata(data_file_name="data_example.xlsx")
