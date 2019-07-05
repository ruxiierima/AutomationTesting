from behave import *
from page_object.home import home
from nose.tools import assert_in,assert_equal


@when("I search product '{product_name}'")
def step_impl(context, product_name):
    home.search_product(product_name)


@then("All the results should be relevant for search '{expected_result}'")
def step_impl(context, expected_result):
    results_list = home.get_list_of_results_name
    for result in results_list:
        assert_in(str(expected_result).upper(), str(result).upper())


@step("I sort results by {sort_method}")
def step_impl(context, sort_method):
    home.choose_sort_method(sort_method)


@then("Results should be displayed by {sort_method}")
def step_impl(context, sort_method):
    displayed_products_price = home.get_list_of_results_price
    expected_list = home.get_list_of_results_price
    if 'Lowest' in sort_method:
        expected_list.sort()
    if 'Highest' in sort_method:
        expected_list.sort(reverse=True)

    assert_equal(displayed_products_price, expected_list)
