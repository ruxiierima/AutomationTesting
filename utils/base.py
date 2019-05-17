import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from utils.driver import Driver
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
class Base():

    TIMEOUT=10
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Base()
        return cls.instance

    def __init__(self):
        self.driver = Driver().get_driver()

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

    ##Types a string into a speciffic field
    def type_into_a_field(self,how,where,what):
        element_field=self.driver.find_element(by=how, value=where)
        if element_field.get_attribute("value") is not None:
            element_field.clear()
        element_field.send_keys(str(what))

    #Checks if a button is already selected
    def check_if_button_is_selected(self,how,where):
        return self.driver.find_element(by=how, value=where).is_selected()

    def select_value_from_dropdown_list(self,how,where,value):
        select = Select(self.driver.find_element(by=how, value=where))
        select.select_by_visible_text(value)

    #value format needs to be like this: 'dd/mm/yyy'
    def type_into_date_box(self,how,where,value):
        element_field = self.driver.find_elements(by=how, value=where)
        self.driver.execute_script("arguments[0].value = arguments[1]", element_field, '01/01/2011')



