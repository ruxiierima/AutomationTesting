from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilis.base import Base
from utilis.element import Element

class SingIn(Base):

    # Class variables and locators
    _sing_in_page_locator = "gr__automationpractice_com"
    _email_address_locator = 'email'
    _password_locator="passwd"

    #Constructor
    #def __init__(self):
       # WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, self._sing_in_page_locator)))

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

    # Clicks on 'Password' field
    def click_password(self):
        pass

    # Clicks on 'Lost your password?' button
    def click_lost_your_password_button(self):
        return self.LostYourPassword()


    class LostYourPassword():

        # Class variables and locators

        # Clicks on 'Email Address' field
        def click_email_address(self):
            pass

        def click_reset_password_button(self):
            pass

        def click_cancel_button(self):
            pass

    class CreateAccount():
        pass





