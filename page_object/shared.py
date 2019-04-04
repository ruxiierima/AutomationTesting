from page_object.home import Home
from utilis.base import Base
from utilis import values
##Common flows
#
#
def sing_in(driver):
    base=Base(driver)
    home=Home(driver)
    base.navigate_to_url(values.BASEURL)
    sing_in = home.click_sing_in_button()
    sing_in.enter_email("abc@gmail.com")
    sing_in.enter_password("pass")