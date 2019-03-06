import unittest

from page_object.home import Home
from utilis import values
from utilis.base import Base
from utilis.driver import Driver

"""Open the site and clicks on SING IN"""


driver=Driver().setUp()

browser = Base(driver)
home = Home(driver)

browser.navigate_to_url(values.BASEURL)
home.click_sing_in_button()