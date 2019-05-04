import logging

from utilis import values

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.remote.webelement import WebElement
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)

## Driver class -setup for the driver
class Driver():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Driver()
        return cls.instance

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def load_website(self):
        self.driver.get(values.BASEURL)

    """def setUp(self):
        global driver
        if driver == None:
            chrome_options = Options()
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--start-maximized")
            driver = webdriver.Chrome(chrome_options=chrome_options)

        return driver"""

    def get_driver(self):
        return self.driver

    # close the browser window
    def tearDown(self):
        self.driver.quit()

web_driver = Driver.get_instance()