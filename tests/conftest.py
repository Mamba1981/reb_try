import os
import json
from core import config
from core.config import get_config
from core.webdriver_manager import get_driver
import pytest


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default=None, help="please choose environment as a must param: --env")
    parser.addoption("--bro", action="store", default=None, help="please choose browser as a must param: --bro")


@pytest.fixture(scope='session')
def env(request):
    env = request.config.getoption('--env')
    if not env:
        with open(os.path.join(config.HOME_PATH, 'tests', 'config.json')) as config_file:
            config_data = json.load(config_file)
    return  config_data['env']


@pytest.fixture(scope='session')
def data(env):
    env_data_files = {
        'dev': 'dev_data.json',
        'qa': 'qa_data.json'
    }
    with open(os.path.join(config.HOME_PATH, 'data', env_data_files[env])) as data_file:
        data = json.load(data_file)
    return data


@pytest.fixture(scope='session')
def driver(request):
    config_browser = request.config.getoption('--bro')
    if not config_browser:
        config_browser = get_config('browser')
    driver = get_driver(config_browser)
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def test_setup(request, env, data, driver):
    request.cls.env = env
    request.cls.data = data
    request.cls.driver = driver


@pytest.fixture(scope="class")
def api_setup(request, env, data):
    request.cls.env = env
    request.cls.data = data


@pytest.fixture(scope="function")  # CREATE FIXTURE SCOPED TO CLASSES
def network_setup(env, data, driver, request):
    request.cls.env = env
    request.cls.data = data
    request.cls.driver = driver


