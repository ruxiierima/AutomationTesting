from behave import *
from page_object.home import home
from page_object.checkout import checkout, address,shipping,payment
from nose.tools import assert_equal


@given("I add {quantity} products to the cart")
def step_impl(context, quantity):
    home.go_to_homescreen()
    home.add_products_in_cart(quantity)


@then("I check if the expected quantity: '{expected_quantity}' added to the cart is correct")
def step_impl(context, expected_quantity):
    current_quantity = home.get_shopping_cart_items
    assert_equal(current_quantity, expected_quantity, "The expected quantity added to the cart is correct")


@when("I click on check out button")
def step_impl(context):
    home.click_on_cart()


@then("I check if all product details from the cart are the same with products from cart summary")
def step_impl(context):
    home.move_to_cart()
    expected_product_details = home.get_all_cart_products_details
    summary_cart_product_details = checkout.get_all_cart_summary_products_details

    assert_equal(expected_product_details[0], summary_cart_product_details[0], 'The product name is correct')
    assert_equal(expected_product_details[1], summary_cart_product_details[1], 'The product price is correct')
    assert_equal(expected_product_details[2], summary_cart_product_details[2], 'The product quantity is correct')


@given("I add product '{specific_items}' to the cart")
def step_impl(context, specific_items):
    home.go_to_homescreen()
    items = specific_items.split(',')

    for specific_item in items:
        home.add_specific_product_in_cart(specific_item)

@when("I go to delivery address")
def step_impl(context):
    home.click_check_out_button()
    checkout.click_on_check_out()

@then("I check delivery address for account: '{email}'")
def step_impl(context, email):
    address.verify_account_information(email)

@when("I choose to pay via {payment_method}")
def step_impl(context,payment_method):
    payment.choose_payment_method(payment_method)

@when("I proceed to checkout")
def step_impl(context):
    context.execute_steps(u"""
        when I go to delivery address
        """)
    checkout.click_on_check_out()
    shipping.agree_to_the_terms()
    checkout.click_on_check_out()


@then("I should be able to submit my order")
def step_impl(context):
    payment.click_confirm_order()
    assert_equal(True, payment.is_order_complete,'The order is complete with chosen payment method')

@then("The confirmation of the {payment_method} payment should be displayed")
def step_impl(context,payment_method):
    assert payment_method.upper() in payment.get_chosen_payment_method.upper()