from selenium.webdriver.common.by import By

from page_object.log_in import LogIn
from utils.base import Base
from utils.driver import web_driver
from utils.element import element


class SingIn(Base):

    instance = None

    # Class variables and locators
    _sing_in_page_locator = "gr__automationpractice_com"
    _email_address_locator_id = 'email'
    _password_locator_id= "passwd"
    _sing_in_button_locator_xpath= "//span[contains(.,'Sign in')]"
    _error_message_locator_class= "alert-danger"
    _create_account_message_class="form_content"
    _create_account_email_field_id="email_create"
    _create_account_button_locator_id='SubmitCreate'

    #Constructor
    def __init__(self):
        self.driver = web_driver.get_driver()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = SingIn()
        return cls.instance

    #Types email on 'Email Address' field from Sing In
    def enter_email(self, email):
        locator=self._email_address_locator_id

        if element.is_element_present(By.ID,locator):
            self.type_into_a_field(By.ID, locator, email)
        else:
            raise TypeError("Element'%s' can not be found" % locator)

    # Types password on 'Password' field from Sing In
    def enter_password(self, password):
        locator=self._password_locator_id

        if element.is_element_present(By.ID,locator):
            self.type_into_a_field(By.ID, locator, password)
        else:
            raise TypeError("Element'%s' can not be found" % locator)

    # Types email on 'Email Address' field from Create An Account
    def enter_email_to_create_account(self,email):
        locator = self._create_account_email_field_id
        if element.is_element_present(By.ID, locator):
            self.type_into_a_field(By.ID ,locator, email)
        else:
            raise TypeError("Element'%s' can not be found" % locator)

    # Clicks on 'Sing In' button
    def click_sing_in_button(self):
        sing_in_button=self.driver.find_element_by_xpath(self._sing_in_button_locator_xpath)
        sing_in_button.click()

    # Clicks on 'CREATE AN ACCOUNT' button
    def click_create_an_account_button(self):
        create_account_button=self.driver.find_element(By.ID,self._create_account_button_locator_id)
        create_account_button.click()
        return LogIn()

    @property
    def get_errot_message(self):
        if element.is_element_present(By.CLASS_NAME, self._error_message_locator_class):
            message=self.driver.find_element_by_class_name(self._error_message_locator_class).text
            return message.split('\n')[1]

    @property
    def get_create_account_message(self):
        locator=self._create_account_message_class
        if element.is_element_present(By.CLASS_NAME, locator):
            current_message=str(self.driver.find_element_by_class_name(locator).text)
            return current_message.split('\n')[0]

sing_in=SingIn.get_instance()




