from modules import *

MAP_MODULE_NAME_TO_CLASS = {
    "search": TestSearchSuite,
    "comment": TestCommentSuite,
}

REQUIRED_PARAM_OF_MUDULE = {
    "search": [],
    "comment": ["post_url"]
}

PARAMS_OF_MODULE_IN_SHEET = {
    "search": ["input_text"],
    "comment": ["input_text"]
}
