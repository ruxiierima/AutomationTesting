from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from nose.tools import assert_equal
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.driver import web_driver
from utils.base import Base


class CheckOut(Base):
    instance = None

    # Class locators
    _checkout_page_locator_id = "order"
    _check_out_id = "button_order_cart"
    _cart_summary_id = "cart_summary"
    _proceed_to_checkout_button_xpath = "(//span[contains(.,'Proceed to checkout')])[2]"
    _checkout_step_css = '.step.clearfix'
    _total_amount_xpath = ".//*[@id='total_price_container']//*[@id='total_price']"
    _shipping_tax_id = "total_shipping"

    def __init__(self):
        self.driver = web_driver.get_driver()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = CheckOut()
        return cls.instance

    # Returns a tuple of lists with all products properties
    @property
    def get_all_cart_summary_products_details(self):
        product_name = []
        products_quantity = []
        products_price = []

        table_id = self.driver.find_element(By.ID, self._cart_summary_id)
        body_element = table_id.find_element(By.TAG_NAME, "tbody")
        rows = body_element.find_elements(By.TAG_NAME, "tr")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight-2000)")
        for row in rows:
            product_properties = row.find_elements(By.TAG_NAME, "td")
            for product_property in product_properties:

                if product_property.get_attribute("class") == 'cart_description':
                    product_name.append(product_property.text.split('\n')[0])

                if product_property.get_attribute("class") == 'cart_unit':
                    price_text = product_property.text
                    product_price = float(price_text.split()[0].split('$')[1])
                    products_price.append(product_price)

                if product_property.get_attribute("class") == 'cart_quantity text-center':
                    product_quantity = product_property.find_element(By.TAG_NAME, 'input').get_attribute("value")
                    products_quantity.append(int(product_quantity))

        return product_name, products_price, products_quantity

    @property
    def get_total_amount(self):
        total_amount_text = self.driver.find_element(By.XPATH, self._total_amount_xpath).text
        return float(total_amount_text.split()[0].split('$')[1])

    @property
    def get_shipping_tax(self):
        shipping_tax_text = self.driver.find_element(By.ID, self._shipping_tax_id).text
        return float(shipping_tax_text.split()[0].split('$')[1])

    def calculate_products_total_price(self):
        products_price = self.get_all_cart_summary_products_details[1]
        return sum(products_price)

    def proceed_to_checkout(self):
        check_out_button = self.driver.find_element(By.ID, self._check_out_id)
        check_out_button.click()

    def click_on_check_out(self):
        button = self._proceed_to_checkout_button_xpath
        self.move_to_element(By.XPATH, button)
        element = self.driver.find_element(By.XPATH, button)
        element.click()


class Address(CheckOut):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Address()
        return cls.instance

    # Class locators
    _delivery_address_id = 'address_delivery'

    def get_delivery_address(self):
        address_information = {'name': None,
                               'address': None,
                               'city_state_postal_code': None,
                               'country': None,
                               'phone': None
                               }

        delivery_address = self.driver.find_element(By.ID, self._delivery_address_id)
        all_information = delivery_address.find_elements(By.TAG_NAME, 'li')
        for information in all_information:

            class_attribute = information.get_attribute('class')

            if class_attribute == 'address_firstname address_lastname':
                address_information['name'] = information.text

            if class_attribute == 'address_address1 address_address2':
                address_information['address'] = information.text

            if class_attribute == 'address_city address_state_name address_postcode':
                address_information['city_state_postal_code'] = information.text

            if class_attribute == 'address_country_name':
                address_information['country'] = information.text

            if class_attribute == 'address_phone_mobile':
                address_information['phone'] = information.text

        return address_information

    def verify_account_information(self, email):
        info_from_csv = self.get_account_info_from_csv(email)
        info_from_web = self.get_delivery_address()
        assert_equal(info_from_csv, info_from_web)


class Shipping(CheckOut):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Shipping()
        return cls.instance

    # Class locators
    _terms_checkbox_class = 'checker'

    def agree_to_the_terms(self):
        self.driver.find_element(By.CLASS_NAME, self._terms_checkbox_class).click()


class Payment(CheckOut):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Payment()
        return cls.instance

    # Class locators
    _payment_methods_xpath = ".//*[@id='HOOK_PAYMENT']//*[@class='row']"
    _summary_payment_css = '.box.cheque-box'
    _confirm_order_button_xpath = "//span[contains(.,'I confirm my order')]"
    _order_status_css = '.alert.alert-success'

    # Choose the payment method for the order
    # payment_method the desired method (available options are: bank/check)
    def choose_payment_method(self, payment_method):
        payment_methods = self.driver.find_elements(By.XPATH, self._payment_methods_xpath)

        for method in payment_methods:
            if payment_method.upper() in method.text.upper():
                method.find_element(By.TAG_NAME, 'a').click()
                break
        else:
            raise Exception("%s not a valid payment method" % payment_method)

    @property
    def get_chosen_payment_method(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._summary_payment_css).text

    def click_confirm_order(self):
        self.driver.find_element(By.XPATH, self._confirm_order_button_xpath).click()

    @property
    def is_order_complete(self):
        try:
            order_status = self.driver.find_element(By.CSS_SELECTOR, self._order_status_css)
            return 'complete' in order_status.text
        except:
            return False


checkout = CheckOut.get_instance()
address = Address.get_instance()
shipping = Shipping.get_instance()
payment = Payment.get_instance()
