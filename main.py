import unittest
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config.config import *


class TestWebModules():
    def __init__(
        self, 
        web_driver_path: str = None, 
        web_url: str = None,
        test_module: str = None
    ):
        self.web_driver_path = web_driver_path if web_driver_path is not None else PATH
        self.web_url = web_url if web_url is not None else WEB_URL
        
        if test_module is None or test_module not in MAP_MODULE_NAME_TO_CLASS.keys():
            raise "test_module must be specified"
        
        self.module_class = MAP_MODULE_NAME_TO_CLASS[test_module]
        
    def test_func(self, input_data: dict):
        suite = unittest.TestSuite()
        suite.addTest(self.module_class(driver_path=self.web_driver_path,
                                        web_url=self.web_url,
                                        **input_data))
        unittest.TextTestRunner().run(suite)     
        
        
if __name__ == "__main__":
    # Ví dụ test module Search
    t = TestWebModules(test_module="search")
    t.test_func(input_data={"input_text": "ascasbhcj", "need_check_output": True})
    