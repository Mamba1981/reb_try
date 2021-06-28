import pytest
from pages.reblaze_home_page import HomePage
import time


@pytest.mark.usefixtures("test_setup")
class TestReblazeHomePage:

    @pytest.mark.abc
    def test_framework(self):
        home_page = HomePage(self.driver, self.env)
        home_page.say_helo()
        self.driver.get("https://yahoo.com")
        time.sleep(10)