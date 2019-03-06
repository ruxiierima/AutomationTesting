import logging

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

    def setUp(self):
        chrome_options = Options()
        # chrome_options.add_argument("–no - sandbox")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver
