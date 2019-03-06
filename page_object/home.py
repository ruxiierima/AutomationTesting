from utilis.base import Base
from utilis.element import Element


class Home(Base):

    #Class locators
    _coockies_locator="//div[@class='cookies-info-text']"
    _accept_button_coockies_locator="fa fa-search"
    _sing_in_button_locator="(//a[@href='/account/login'][contains(.,'Sign In / Create Account')])[3]"


    def click_accept_button(self):
        self.driver.implicitly_wait(30)
        accept_button = self.driver.find_element_by_class_name(self._accept_button_coockies_locator)
        #accept_button=self.driver.switch_to.frame(self.driver.find_element_by_xpath(self._accept_button_coockies_locator))
        accept_button.click()

    def click_sing_in_button(self):
        self.driver.implicitly_wait(30)
        sing_in_button= self.driver.find_element_by_xpath(self._sing_in_button_locator)
        sing_in_button.click()