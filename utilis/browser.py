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

try:
    from utilis.navigation import Navigation
except ImportError:
    logging.critical("navigation.py is missing...Exiting program.")
    exit(1)

## Browser class -setup for the browser
class Browser(Navigation):

    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    driver= webdriver.Chrome(chrome_options=chrome_options)

    def open_webpage(self):
        self.driver.get(values._base_url)

    def exit_browser(self):
        self.driver.quit()

    def delete_cookies(self):
        self.driver.delete_all_cookies()

