import logging
import os

try:
    from selenium import webdriver
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
# Navivation - Navigation class from navigation.py
class Browser(Navigation):

    #webdriver = "C:\Users\ierima\PycharmProjects\AutomationTesting\utilis\chromedriver.exe"
    driver= webdriver.Chrome()

    def open_webpage(self):
        self.driver.get("https://topodesigns.com")

    def exit_browser(self):
        self.driver.quit()

