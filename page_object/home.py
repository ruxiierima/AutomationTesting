from utils.base import Base
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from page_object.checkout import CheckOut
from page_object.sing_in import SingIn
from utils.driver import web_driver
from utils.element import element


class Home(Base):
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
    _sing_out_button_class = 'logout'
    _account_name_class = 'account'
    _product_list_class = "product-container"
    _shopping_cart_class= "shopping_cart"
    _continue_shopping_locator_xpath = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span'
    _cart_products_class='products'

    def click_sing_in_button(self):
        sing_in_button = self.driver.find_element_by_class_name(self._sing_in_button_locator)
        sing_in_button.click()
        return SingIn()

    def click_sing_out_button(self):
        self.driver.implicitly_wait(10)
        sing_out_button = self.driver.find_element(By.CLASS_NAME, self._sing_out_button_class)
        sing_out_button.click()

    @property
    def already_sing_in(self):
        return element.is_element_present(By.CLASS_NAME,self._sing_out_button_class)

    @property
    def get_account_name(self):
        element = self.driver.find_element(By.CLASS_NAME, self._account_name_class)
        return element.text

    def add_products_in_cart(self,quantity):
        wait = WebDriverWait(self.driver, 20)
        product_containers_id = self.driver.find_element(By.ID, "homefeatured")
        product_containers = product_containers_id.find_elements_by_tag_name("li")

        for index, product in enumerate(product_containers):
            if index == quantity:
                break
            i = index + 1
            hover = ActionChains(self.driver).move_to_element(product)
            hover.perform()
            #self.driver.switch_to.default_content()
            _add_to_cart_locator_xpath='//*[@id="homefeatured"]/li[%s]/div/div[2]/div[2]/a[1]/span'%i
            wait.until(EC.element_to_be_clickable((By.XPATH,_add_to_cart_locator_xpath)))
            self.driver.implicitly_wait(2)
            add_product = self.driver.find_element(By.XPATH,_add_to_cart_locator_xpath)
            ActionChains(self.driver).move_to_element(add_product).click()

            wait.until(EC.element_to_be_clickable((By.XPATH, self._continue_shopping_locator_xpath)))
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, self._continue_shopping_locator_xpath ).click()

    @property
    def get_shopping_cart_items(self):
        element=self.driver.find_element(By.CLASS_NAME, self._shopping_cart_class)
        text=element.text
        for char in text:
            if char.isdigit():
                return char
        else:
            return text

    @property
    def get_number_of_items(self):
        cart_elements = self.driver.find_element(By.CLASS_NAME,self._cart_products_class).find_elements(By.TAG_NAME,'dt')
        return len(cart_elements)

    @property
    def get_all_cart_products_details(self):
        products_name = []
        products_price = []
        products_quantity = []

        product_list = self.driver.find_element(By.CLASS_NAME, self._cart_products_class).find_elements(By.TAG_NAME,
                                                                                                        'dt')
        for product in product_list:
            cart_info = product.find_element(By.CLASS_NAME, 'cart-info')

            product_name = (cart_info.find_element(By.XPATH, ".//*[@class='cart_block_product_name']")).get_attribute(
                'title')
            products_name.append(product_name)

            product_price = float(( cart_info.find_element(By.XPATH, ".//*[@class='price']").text).split()[0].split('$')[1])
            products_price.append(product_price)

            product_quantity=int(cart_info.find_element(By.XPATH,".//*[@class='quantity']").text)
            products_quantity.append(product_quantity)

        return products_name, products_price, products_quantity


    def move_to_cart(self):
        ActionChains(self.driver).move_to_element(
        self.driver.find_element(By.XPATH, "//b[contains(.,'Cart')]")).perform()

    def click_on_cart(self):
        self.driver.find_element(By.XPATH,"//b[contains(.,'Cart')]").click()
        return CheckOut()

home = Home.get_instance()
