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
    _cookies_locator = "//div[@class='cookies-info-text']"
    _sing_in_button_locator = "login"
    _sing_out_button_class = 'logout'
    _account_name_class = 'account'
    _products_container_id = 'homefeatured'
    _product_list_class = "product-container"
    _shopping_cart_class = "shopping_cart"
    _continue_shopping_locator_xpath = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span'
    _cart_products_class = 'products'
    _proceed_to_checkout_xpath = "//span[contains(.,'Proceed to checkout')]"
    _check_out_cart_xpath = "//span[contains(.,'Check out')]"
    _logo_button_css = '.logo.img-responsive'
    _search_field_id = "search_query_top"
    _search_results_css = '.product_list.grid.row'
    _sort_method_xpath = ".//*[@id='productsSortForm']//*[@id='selectProductSort']"

    @property
    def already_sing_in(self):
        return element.is_element_present(By.CLASS_NAME, self._sing_out_button_class)

    @property
    def get_account_name(self):
        account_name = self.driver.find_element(By.CLASS_NAME, self._account_name_class)
        return account_name.text

    @property
    def get_shopping_cart_items(self):
        shopping_cart = self.driver.find_element(By.CLASS_NAME, self._shopping_cart_class)
        text = shopping_cart.text
        for char in text:
            if char.isdigit():
                return char
        else:
            return text

    @property
    def get_number_of_items(self):
        cart_elements = self.driver.find_element(By.CLASS_NAME, self._cart_products_class).find_elements(By.TAG_NAME,
                                                                                                         'dt')
        return len(cart_elements)

    @property
    def get_list_of_products(self):
        product_containers_id = self.driver.find_element(By.ID, self._products_container_id)
        return product_containers_id.find_elements_by_tag_name("li")

    @property
    def get_list_of_results_name(self):
        products_name = []

        product_containers = self.driver.find_element(By.CSS_SELECTOR, self._search_results_css)
        product_list = product_containers.find_elements_by_tag_name("li")
        for product in product_list:
            name = product.text.split('\n')[0]
            if name is not "":
                products_name.append(product.text.split('\n')[0])
        return products_name

    @property
    def get_list_of_results_price(self):
        products_price = []

        product_containers = self.driver.find_element(By.CSS_SELECTOR, self._search_results_css)
        product_list = product_containers.find_elements_by_tag_name("li")
        for product in product_list:
            name = product.text.split('\n')[0]
            if name is not "":
                price_text = product.text.split('\n')[1]
                products_price.append(float(price_text.split()[0].split('$')[1]))
        return products_price

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

            product_price = float(
                cart_info.find_element(By.XPATH, ".//*[@class='price']").text.split()[0].split('$')[1])
            products_price.append(product_price)

            product_quantity = int(cart_info.find_element(By.XPATH, ".//*[@class='quantity']").text)
            products_quantity.append(product_quantity)

        return products_name, products_price, products_quantity

    def search_product(self, product_name):
        self.type_into_a_field(By.ID, self._search_field_id, product_name)
        self.driver.find_element(By.ID, self._search_field_id).submit()

    def add_products_in_cart(self, quantity):
        wait = WebDriverWait(self.driver, self.TIMEOUT)

        product_containers = self.get_list_of_products

        for index, product in enumerate(product_containers):
            if index == int(quantity):
                break
            i = index + 1
            hover = ActionChains(self.driver).move_to_element(product)
            hover.perform()

            _add_to_cart_locator_xpath = '//*[@id="homefeatured"]/li[%s]/div/div[2]/div[2]/a[1]/span' % i
            wait.until(EC.element_to_be_clickable((By.XPATH, _add_to_cart_locator_xpath)))
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, _add_to_cart_locator_xpath).click()

            wait.until(EC.element_to_be_clickable((By.XPATH, self._continue_shopping_locator_xpath)))
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, self._continue_shopping_locator_xpath).click()

    # Add specific product to the cart by name
    # product_name - The name of the desired product
    def add_specific_product_in_cart(self, desired_product_name):
        wait = WebDriverWait(self.driver, self.TIMEOUT)
        product_containers = self.get_list_of_products

        for index, product in enumerate(product_containers):
            product_name = product.text.split('\n')[0]
            if desired_product_name == product_name:
                hover = ActionChains(self.driver).move_to_element(product)
                hover.perform()
                i = index + 1
                _add_to_cart_locator_xpath = '//*[@id="homefeatured"]/li[%s]/div/div[2]/div[2]/a[1]/span' % i
                wait.until(EC.element_to_be_clickable((By.XPATH, _add_to_cart_locator_xpath)))
                self.driver.implicitly_wait(2)
                self.driver.find_element(By.XPATH, _add_to_cart_locator_xpath).click()
                self.driver.find_element(By.XPATH, self._continue_shopping_locator_xpath).click()
                break
        else:
            raise Exception("Product '%s' not fount" % desired_product_name)

    def go_to_homescreen(self):
        self.driver.find_element(By.CSS_SELECTOR, self._logo_button_css).click()

    def click_sing_in_button(self):
        sing_in_button = self.driver.find_element_by_class_name(self._sing_in_button_locator)
        sing_in_button.click()
        return SingIn()

    def click_sing_out_button(self):
        self.driver.implicitly_wait(10)
        sing_out_button = self.driver.find_element(By.CLASS_NAME, self._sing_out_button_class)
        sing_out_button.click()

    def click_check_out_button(self):
        self.move_to_cart()
        self.driver.find_element(By.XPATH, self._check_out_cart_xpath).click()
        return CheckOut()

    def move_to_cart(self):
        self.move_to_element(By.XPATH, "//b[contains(.,'Cart')]")

    def click_on_cart(self):
        self.driver.find_element(By.XPATH, "//b[contains(.,'Cart')]").click()
        return CheckOut()

    def choose_sort_method(self, method):
        self.select_value_from_dropdown_list(By.XPATH, self._sort_method_xpath, method)


home = Home.get_instance()
