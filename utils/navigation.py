import time
import logging

from utils.base import Base

try:
    from selenium import webdriver
    from selenium.common.exceptions import WebDriverException
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)

## Navigation class - commun function for browser navigation
class Navigation():

    def back(self,driver):
        try:
            driver.back()
        except WebDriverException:
            logging.error("WebDriverException: Couldn't return to previous page")

    def forward(self):
        try:
            self.driver.forward()
        except WebDriverException:
            logging.error("WebDriverException: Couldn't forward to next page")

    def refresh(self):
        try:
            self.driver.refresh()
        except WebDriverException:
            logging.error("WebDriverException: Couldn't refresh the page")
