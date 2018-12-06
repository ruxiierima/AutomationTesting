from utilis import browser

class PageObject():
    def is_object_visible(self,object):
        return object.is_displayed()