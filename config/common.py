from modules import *

MAP_MODULE_NAME_TO_CLASS = {
    "search": TestSearchSuite,
    "comment": TestCommentSuite,
    "sendMessage": TestSendMassage,
    "changePassword": TestChangePassword,
    "profile": TestProfileSuite,
    "signin": TestSignInSuite
}

REQUIRED_PARAM_OF_MUDULE = {
    "search": [],
    "comment": ["post_url"],
    "sendMessage": ["post_url"],
    "changePassword": ["post_url"],
    "profile": [],
    "signin": []
}

PARAMS_OF_MODULE_IN_SHEET = {
    "search": ["input_text"],
    "comment": ["input_text"]
}
