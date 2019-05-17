from utils.driver import web_driver

def before_all(context):
    context.browser=web_driver.get_driver()

#def after_all(context):
  #  context.browser.close()