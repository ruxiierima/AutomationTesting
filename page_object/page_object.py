from utilis import base

class PageObject():


    def is_object_visible(self,object):
        return object.is_displayed()