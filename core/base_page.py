from selenium.webdriver.remote.webdriver import *


class BasePage:

    def __init__(self, driver: WebDriver=None, env=None):
        self.driver = driver
        self.env = env