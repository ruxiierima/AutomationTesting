from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilis.base import Base
from utilis.element import Element

class SingIn(Base):

    # Class variables and locators
    _sing_in_page_locator = "gr__automationpractice_com"
    _email_address_locator = 'email'

    #Constructor
    #def __init__(self):
       # WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, self._sing_in_page_locator)))

    #Clicks on 'Email Address' field
    def click_email_address(self):
        Element(self.driver).click_on_element(self._email_address_locator,'id')

    def write_email(self,email):
        element=Element(self.driver).find_element_by(self._email_address_locator,'id')
        element.send_keys(email)

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





