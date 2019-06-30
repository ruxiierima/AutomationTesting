import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.data_handler import DataHandler
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

    TIMEOUT = 10
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

    def move_to_element(self,  how, what):
        element = self.driver.find_element(by=how, value=what)
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

    def select_radio_button(self,how,where,value):
        radio_buttons = self.driver.find_elements(by=how,value=where)
        for item in radio_buttons:
            if value in item.text and not item.is_selected():
                item.click()

    #value format needs to be like this: 'dd/mm/yyy'
    def type_into_date_picker(self,how,where,value):
        data_list=str(value).split('/')
        dictionary_data={'days':None ,
                         'months':None ,
                         'years':None
                         }

        for index, key in enumerate(dictionary_data):
                dictionary_data[key]=(data_list[index])

        data_elements= self.driver.find_elements(by=how, value=where)

        for index,item in enumerate(data_elements):
            element=item.find_element(By.ID,str(list(dictionary_data.keys())[index]))
            Select(element).select_by_value(data_list[index])

    def get_acount_info_from_csv(self,email):
        account_information={'name':None,
                         'address':None,
                         'city_state_postal_code':None,
                         'country':None,
                         'phone':None
                         }

        account_name = DataHandler().test_data('first_name',email) + " " + DataHandler().test_data('last_name',email)
        account_information['name'] = account_name

        account_address = str(DataHandler().test_data('address_1',email))
        account_information['address'] = account_address

        account_city_state_postal = DataHandler().test_data('city',email) + ", "\
                                    + DataHandler().test_data('state',email)+ " " + str(DataHandler().test_data('postal_code',email))
        account_information['city_state_postal_code']=account_city_state_postal

        account_country = DataHandler().test_data('country',email)
        account_information['country']=account_country

        account_phone = str(DataHandler().test_data('mobile_phone',email))
        account_information['phone']=account_phone

        return account_information



