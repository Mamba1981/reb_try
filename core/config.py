import os
import json

HOME_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

__config_data = None


def __load_config():
    global __config_data
    with open(HOME_PATH + os.path.sep + 'tests' + os.path.sep + 'config.json') as config_file:
        __config_data = json.load(config_file)
    return __config_data


def get_config(key: str):
    if __config_data is None:
        __load_config()
    if key not in __config_data:
        raise Exception('The config file does not contain' + key.upper() + " key")
    if key == 'browser' and __config_data['browser'] not in get_config('supported-browsers'):
        raise Exception("The following browser is not supported" + __config_data['browser'])
    return __config_data[key]