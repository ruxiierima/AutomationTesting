from page_object.sing_in import SingIn
from utilis.base import Base
from utilis.element import Element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home(Base):

    #Class locators
    _home_page_locator="gr__automationpractice_com"
    _coockies_locator="//div[@class='cookies-info-text']"
    _sing_in_button_locator="login"

    ## Constructor who waits for page to pe loaded

        #WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, self._home_page_locator)))


    def click_sing_in_button(self):
        sing_in_button= self.driver.find_element_by_class_name(self._sing_in_button_locator)
        sing_in_button.click()
        return SingIn(self.driver)