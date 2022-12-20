import os
from dotenv import load_dotenv

PROJ_PATH = os.getcwd()
load_dotenv()

class Config:
    driver_path = PROJ_PATH + "/chromedriver/chromedriver.exe"
    web_url = "https://tinhte.vn/"
    web_username = os.getenv("WEB_USERNAME")
    web_password = os.getenv("WEB_PASSWORD")

    input_data_folder = PROJ_PATH + "/data/input_data"
    output_data_folder = PROJ_PATH + "/data/output_data"
