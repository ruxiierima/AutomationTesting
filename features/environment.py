from utils.driver import web_driver, Driver

def before_all(context):
    web_driver.get_instance()
    context.browser=web_driver.get_driver()

#def after_all(context):
    #context.browser.close()

# -- BEHAVE HOOKS:
def before_feature(context, feature):
     if 'setup' in feature.tags:
        context.browser.delete_all_cookies()

#def after_feature(context,feature):
    #if 'setup' in feature.tags:



