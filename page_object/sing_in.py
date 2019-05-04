from selenium.webdriver.common.by import By

from utilis.base import Base
from utilis.driver import web_driver
from utilis.element import element


class SingIn(Base):

    instance = None

    # Class variables and locators
    _sing_in_page_locator = "gr__automationpractice_com"
    _email_address_locator = 'email'
    _password_locator="passwd"
    _sing_in_button_locator="//span[contains(.,'Sign in')]"
    _error_message_locator="alert alert-danger"

    #Constructor
    def __init__(self):
        self.driver = web_driver.get_driver()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = SingIn()
        return cls.instance

    #Types email on 'Email Address' field
    def enter_email(self, email):
        element=self.driver.find_element_by_id(self._email_address_locator)
        if self.is_element_visible(element):
            self.type_into_a_field(element,email)
        else:
            raise TypeError("Element'%s' can not be found"%self._email_address_locator)

    # Types password on 'Password' field
    def enter_password(self, password):
        element = self.driver.find_element_by_id(self._password_locator)
        if self.is_element_visible(element):
            self.type_into_a_field(element, password)
        else:
            raise TypeError("Element'%s' can not be found" % self._password_locator)

    # Clicks on 'Sing In' button
    def click_sing_in_button(self):
        sing_in_button=self.driver.find_element_by_xpath(self._sing_in_button_locator)
        sing_in_button.click()
        return self.SingInAuthentication()

    class SingInAuthentication():

        # Class variables and locators
        _error_message_locator = "alert alert-danger"

        def is_error_message_present(self):
            return element.is_element_present(By.CLASS_NAME,self._error_message_locator)

sing_in=SingIn.get_instance()




