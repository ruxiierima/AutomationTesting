from page_object.sing_in import SingIn
from utilis.driver import web_driver


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

    def click_sing_in_button(self):
        sing_in_button= self.driver.find_element_by_class_name(self._sing_in_button_locator)
        sing_in_button.click()
        return SingIn()


home = Home.get_instance()