PATH = "chromedriver/chromedriver.exe"
WEB_URL = "https://tinhte.vn/"


from modules import TestSearchSuite
MAP_MODULE_NAME_TO_CLASS = {
    "search": TestSearchSuite,
    "comment": None,
}