# -- BEHAVE HOOKS

from utils.driver import web_driver
from page_object.home import home


def before_all(context):
    web_driver.get_instance()
    context.browser = web_driver.get_driver()


def after_all(context):
    context.browser.quit()


def before_feature(context, feature):
    if 'setup' in feature.tags:
        context.browser.delete_all_cookies()
        if home.already_sing_in:
            home.click_sing_out_button()


"""
def after_feature(context,feature):
    if 'setup' in feature.tags:
        context.browser.close()
"""
