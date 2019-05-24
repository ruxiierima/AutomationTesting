
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utils.base import Base
from utils.driver import web_driver
from utils.element import element


class LogIn(Base):

    instance=None

    #Class variables
    _log_in_page_locator_class='account-creation_form'
    _gender_list_xpath='radio-inline'
    _first_name_text_box_id='customer_firstname'
    _first_name_address_text_box_id='firstname'
    _last_name_text_box_id='customer_lastname'
    _last_name_address_text_box_id = 'lastname'
    _password_text_box_id='passwd'
    _address_text_box_id='address1'
    _post_code_text_box_id='postcode'
    _additional_info_text_box_id='other'
    _mobile_phone_text_box_id='phone_mobile'
    _alias_address_text_box_id='alias'
    _city_text_box_id='city'
    _state_text_box_id='id_state'
    _country_text_box_id='id_country'
    _dob_data_box_class='col-xs-4'
    _register_button_xpath="//span[contains(.,'Register')]"

    # Constructor
    def __init__(self):
        self.driver = web_driver.get_driver()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LogIn()
        return cls.instance

    #Choose the gender by clicking an option from Title field
    def select_gender(self,gender):

        #WebDriverWait(self.driver,30).until((lambda x: x.find_element(By.CLASS_NAME, self._log_in_page_locator_class)))
        self.driver.implicitly_wait(self.TIMEOUT)

        gender_list=self.driver.find_elements(By.CLASS_NAME,self._gender_list_xpath)

        for item in gender_list:
            if gender in item.text and not item.is_selected() :
                item.click()

    #Fill all the TEXT BOXES

    def enter_first_name(self,first_name):
        self.type_into_a_field(By.ID ,self._first_name_text_box_id,first_name)

    def enter_first_name_address(self,first_name_address):
        self.type_into_a_field(By.ID, self._first_name_address_text_box_id, first_name_address)

    def enter_last_name(self,last_name):
        self.type_into_a_field(By.ID, self._last_name_text_box_id,last_name)

    def enter_last_name_address(self, last_name_address):
        self.type_into_a_field(By.ID, self._last_name_address_text_box_id, last_name_address)

    def enter_password(self,passw):
        self.type_into_a_field(By.ID,self._password_text_box_id,passw)

    def enter_address(self,address):
        self.type_into_a_field(By.ID, self._address_text_box_id, address)

    def enter_post_code(self,post_code):
        self.type_into_a_field(By.ID, self._post_code_text_box_id, post_code)

    def enter_additional_info(self,additional_info):
        self.type_into_a_field(By.ID, self._additional_info_text_box_id, additional_info)

    def enter_mobile_phone(self,mobile_phone):
        self.type_into_a_field(By.ID, self._mobile_phone_text_box_id, mobile_phone)

    def enter_alias_address(self,alias_address):
        self.type_into_a_field(By.ID, self._alias_address_text_box_id, alias_address)

    def enter_city(self,city):
        self.type_into_a_field(By.ID, self._city_text_box_id,city)

    def choose_state(self,state):
        self.select_value_from_dropdown_list(By.ID,self._state_text_box_id,state)

    def choose_country(self, country):
        self.select_value_from_dropdown_list(By.ID, self._country_text_box_id, country)

    def enter_dob(self,dob):
        self.type_into_date_picker(By.CLASS_NAME,self._dob_data_box_class,dob)

    def click_register(self):
        self.driver.find_element(By.XPATH,self._register_button_xpath).click()

log_in=LogIn.get_instance()