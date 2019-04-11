import logging
from selenium.webdriver.common.action_chains import ActionChains

from utilis.driver import Driver
from behave import given, when, then
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.remote.webelement import WebElement
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)

## Base class -helper functionality
class Base(Driver):

    def __init__(self, driver):
        self.driver = driver

    @given(u'I navigate to the url: {url} the website')
    def navigate_to_url(self, url):
        if isinstance(url, str):
            self.driver.get(url)
        else:
            raise TypeError("URL must be a string.")

    def exit_browser(self):
        self.driver.quit()

    def delete_cookies(self):
        self.driver.delete_all_cookies()

    def move_to_element(self, element_locator):
        element = self.driver.find_element_by_id(element_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    ##Checks if an element is visible
    def is_element_visible(self,element):
        return element.is_displayed()

    def find_element_by(self,locator,option):
        if option=='id':
            return self.driver.find_element_by_id(locator)
        if option=='class':
            return self.driver.find_element_by_class_name(locator)
        else:
            raise Exception("Not a valid option!")

    ##Types a string into a speciffic field
    def type_into_a_field(self,field_element,string):
        field_element.send_keys(string)


