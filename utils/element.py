import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import web_driver

try:
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import NoSuchElementException

except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)


## Element- commun function for page elements
class Element():
    instance = None

    def __init__(self):
        self.driver = web_driver.get_driver()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Element()
        return cls.instance

    def click_on_element(self, element_locator, option):
        element = self.driver.find_element_by(element_locator, option)
        element.click()

    def find_element_by(self, locator, option):
        if option == 'id':
            return self.driver.find_element_by_id(locator)
        if option == 'class':
            return self.driver.find_element_by_class_name(locator)
        else:
            raise Exception("Not a valid option!")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
            return True
        except NoSuchElementException as e:
            return False


element = Element.get_instance()
