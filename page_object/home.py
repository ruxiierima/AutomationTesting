from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from page_object.sing_in import SingIn
from utils.driver import web_driver


class Home():

    instance = None

    def __init__(self):
        self.driver = web_driver.get_driver()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Home()
        return cls.instance

    # Class locators
    _home_page_locator = "gr__automationpractice_com"
    _coockies_locator = "//div[@class='cookies-info-text']"
    _sing_in_button_locator = "login"
    _sing_out_button_class='logout'
    _account_name_class='account'
    _product_list_class="product-container"
    _continue_shopping_locator_xpath="(//span[contains(.,'Continue shopping')])[2]"


    def click_sing_in_button(self):
        sing_in_button= self.driver.find_element_by_class_name(self._sing_in_button_locator)
        sing_in_button.click()
        return SingIn()

    def click_sing_out_button(self):
        self.driver.implicitly_wait(10)
        sing_out_button= self.driver.find_element(By.CLASS_NAME,self._sing_out_button_class)
        sing_out_button.click()

    @property
    def get_account_name(self):
        element=self.driver.find_element(By.CLASS_NAME,self._account_name_class)
        return element.text

    def add_products_in_cart(self):
        product_containers=self.driver.find_elements(By.CLASS_NAME,self._product_list_class)

        for index,product in enumerate(product_containers):
            index+=1
            hover=ActionChains(self.driver).move_to_element(product)
            hover.perform()
            self.driver.find_element(By.XPATH,"(//span[contains(.,'Add to cart')])[%s]" %index).click()

            wait = WebDriverWait(self.driver, 20)
            element=wait.until(EC.visibility_of_element_located((By.XPATH,self._continue_shopping_locator_xpath)))
            self.driver.find_element(By.XPATH,self._continue_shopping_locator_xpath).click()

home = Home.get_instance()