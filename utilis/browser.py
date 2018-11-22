import logging

try:
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.remote.webelement import WebElement
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)

try:
    from navigation import Navigation
except ImportError:
    logging.critical("navigation.py is missing...Exiting program.")
    exit(1)

## Browser class -setup for the browser
# Navivation - Navigation class from navigation.py
class Browser(Navigation):
    driver = None

    def __init__(self,driver):
        self.driver = driver

