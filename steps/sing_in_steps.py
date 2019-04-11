from behave import *
from behave import step
from utilis import values
from page_object.home import Home
from utilis.base import Base
from utilis.driver import Driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@step ("I sing in with email: {email} and password: {password}")
def step(context,email,password):
    driver = Driver().setUp()
    step.emailData=[email]
    step.passData = [password]

    base = Base(driver)
    home = Home(driver)
    base.navigate_to_url(values.BASEURL)
    sing_in = home.click_sing_in_button()
    sing_in.enter_email(email)
    sing_in.enter_password(password)
