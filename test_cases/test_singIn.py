import unittest
from unittest import TestCase

from selenium import webdriver

from page_object import shared
from utilis import values
from utilis.base import Base
from utilis.driver import Driver

"""Open the site and clicks on SING IN"""

class TestSingIn(TestCase):
    # SetUp function
    def setUp(self):
        self.driver = webdriver.Chrome()
        # driver=Driver().setUp()

    def test_sing_in(self):
        shared.sing_in(self.driver,"email",'pass')
        assert 'My' in self.driver.title


    # Driver().tearDown()

    if __name__ == "__main__":
        unittest.main()
