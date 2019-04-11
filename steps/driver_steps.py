from behave import step
from pip._internal.utils import logging
from behave import use_fixture
from utilis.driver import Driver

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.remote.webelement import WebElement
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)

@step("I set up the browser")
def setUp(context):
    chrome_options = Options()
    # chrome_options.add_argument("–no - sandbox")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # self.driver.implicitly_wait(30)

def before_tag(context, tag):
    if tag == "fixture.browser.chrome":
        use_fixture(Driver.setUp(), context, timeout=10)


