from behave import *
from page_object.home import home
from page_object.checkout import checkout
from nose.tools import assert_equal


@given("I add {quantity} products to the cart")
def step_impl(context,quantity):
    home.add_products_in_cart(quantity)

@then("I check if the expected quantity: '{expected_quantity}' added to the cart is correct")
def step_impl(context,expected_quantity):
    current_quantity=home.get_shooping_cart_items
    assert_equal(expected_quantity,current_quantity,"The expected quantity added to the cart is correct")

@when("I click on check out button")
def step_impl(context):
    home.click_on_cart()

@then("I check if all product details from cart summary are the same with products from the cart")
def step_impl(context):
    home.move_to_cart()
    expected_product_details = home.get_all_cart_products_details
    summary_cart_product_details = checkout.get_all_cart_summary_products_details

    assert_equal(expected_product_details[0],summary_cart_product_details[0],'The product name is correct')
    assert_equal(expected_product_details[1], summary_cart_product_details[1], 'The product price is correct')
    assert_equal(expected_product_details[2], summary_cart_product_details[2], 'The product quantity is correct')