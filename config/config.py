import os
from dotenv import load_dotenv

PROJ_PATH = os.getcwd()
load_dotenv()


class Config:
    driver_path = PROJ_PATH + "/chromedriver/chromedriver.exe"
    web_url = os.getenv("WEB_URL", "https://tinhte.vn/")
    web_username = os.getenv("WEB_USERNAME")
    web_password = os.getenv("WEB_PASSWORD")
    locator_wait_time = int(os.getenv("WAIT_TIME", 10))

    input_data_folder = PROJ_PATH + "/data/input_data"
    output_data_folder = PROJ_PATH + "/data/output_data"
