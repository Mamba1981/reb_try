import os
import json
from core.config import HOME_PATH

__login_data = None


def __load_login_json():
    global __login_data
    with open(HOME_PATH + os.path.sep + 'login_data.json') as login_data_file:
        __login_data = json.load(login_data_file)
    return __login_data


def get_login_data(env: str, key: str):
    if __login_data is None:
        __load_login_json()
    return __login_data[env][key]