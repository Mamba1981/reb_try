import os
from core import config
from core.config import get_config
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(requested_browser):
    browsers_dict = {
        "chrome": __get_local_chrome,
        "chrome_linux": __get_local_chrome_linux,
        "chrome_remote": __get_remote_chrome,
        "firefox": __get_local_firefox,
        "responsive": __get_responsive
    }
    try:
        return browsers_dict[requested_browser]()
    except Exception as e:
        print("Browser not supported, could not load driver: " + str(e))


def __get_local_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    chrome_driver = webdriver.Chrome(os.path.join(config.HOME_PATH, 'drivers', 'chrome', 'chromedriver'), options=options)


def __get_local_chrome_linux():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--allow-running-inscure-content')
    options.add_argument("--window-size=1920x1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-notifications")
    # chrome_driver = webdriver.Chrome(config.HOME_PATH + sep + 'drivers' + sep + 'linux_driver' + sep + 'chromedriver', options=options)
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return chrome_driver

# def __get_local_firefox():
#     profile = webdriver.FirefoxProfile()
#     profile.accept_untrusted_certs = True
#     firefox_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     return firefox_driver


def __get_local_firefox():
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--allow-running-insecure-content')
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--ignore-ssl-errors')
    # options.add_argument("--start-maximized")
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920x1080")
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # firefox_driver = webdriver.Firefox(GeckoDriverManager().install(), options=options)
    src = os.path.join(config.HOME_PATH, 'drivers', 'gecko')
    firefox_driver = webdriver.Firefox(os.path.join(config.HOME_PATH, 'drivers', 'gecko'))
    return firefox_driver


def __get_remote_chrome():
    hub_address = get_config('hub-address')
    from selenium.webdriver.chrome.options import Options as ChromeOptions

    chrome_options = ChromeOptions()
    return webdriver.Remote(hub_address, chrome_options.to_capabilities())


def __get_responsive():
    options = webdriver.ChromeOptions()
    mobile_emulation = {"deviceName": "iPhone X"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_driver = webdriver.Chrome(os.path.join(config.HOME_PATH, 'drivers', 'chromedriver'), options=options)
    return chrome_driver