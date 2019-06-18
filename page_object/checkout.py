from selenium.webdriver.common.by import By
from utils.driver import web_driver
from utils.base import Base

class CheckOut(Base):
    instance = None

    # Class locators
    _checkout_page_locator_id = "order"
    _check_out_id = "button_order_cart"
    _cart_summary_id = "cart_summary"

    def __init__(self):
        self.driver = web_driver.get_driver()
        #WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, self._checkout_page_locator_id)))

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = CheckOut()
        return cls.instance

    def proceed_to_checkout(self):
        check_out_button = self.driver.find_element(By.ID, self._check_out_id)
        check_out_button.click()

    #Returns a tuple of lists with all products properties
    @property
    def get_all_cart_summary_products_details(self):
        product_name=[]
        products_quantity=[]
        products_price=[]

        table_id=self.driver.find_element(By.ID,self._cart_summary_id)
        body_element = table_id.find_element(By.TAG_NAME, "tbody")
        rows = body_element.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            product_properties=row.find_elements(By.TAG_NAME,"td")
            for product_property in product_properties:

                if product_property.get_attribute("class") == 'cart_description':
                    product_name.append(product_property.text.split('\n')[0])

                if product_property.get_attribute("class") == 'cart_unit':
                    price_text=product_property.text
                    product_price=float(price_text.split()[0].split('$')[1])
                    products_price.append(product_price)

                if product_property.get_attribute("class") == 'cart_quantity text-center':
                    product_quantity=product_property.find_element(By.TAG_NAME,'input').get_attribute("value")
                    products_quantity.append(int(product_quantity))

        return product_name, products_price,products_quantity

checkout = CheckOut.get_instance()