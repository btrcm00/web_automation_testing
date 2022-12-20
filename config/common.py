from modules import *

MAP_MODULE_NAME_TO_CLASS = {
    "search": TestSearchSuite,
    "comment": TestCommentSuite,
}

REQUIRED_PARAM_OF_MUDULE = {
    TestSearchSuite: [],
    TestCommentSuite: ["web_login_func", "post_url"]
}
