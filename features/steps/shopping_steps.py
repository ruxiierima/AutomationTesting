from behave import *
from page_object.home import home

use_step_matcher("re")


@given("I add products to the cart")
def step_impl(context):
    home.add_products_in_cart()