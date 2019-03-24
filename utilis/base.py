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

## Browser class -setup for the browser
class Base():

    def __init__(self,driver):
        self.driver= driver

    def navigate_to_url(self, url):
        if isinstance(url, str):
            self.driver.get(url)
        else:
            raise TypeError("URL must be a string.")

    def exit_browser(self):
        self.driver.quit()

    def delete_cookies(self):
        self.driver.delete_all_cookies()
