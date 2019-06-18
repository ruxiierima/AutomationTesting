from behave import *
from nose.tools import assert_equal
from page_object.sing_in import sing_in
from page_object.log_in import log_in
from page_object.home import home
from utils.driver import web_driver
from utils.data_handler import DataHandler
import logging

random_email = DataHandler().generate_random_emails()


@given("I load the website")
def step(context):
    web_driver.load_website()


@given("I go to Sing In page")
def step_impl(context):
    home.click_sing_in_button()


@given("I sing in with email:{email} and pass:{password}")
def step_impl(context, email, password):
    sing_in.enter_email(email)
    sing_in.enter_password(password)


@when("I press the Sing In button")
def step_impl(context):
    sing_in.click_sing_in_button()


@then("I check if the expected error message:{expected_message} is displayed in Sing In field")
def step_impl(context, expected_message):
    assert_equal(expected_message, sing_in.get_errot_message, "The error message is displayed")


@given("I insert random email into 'Create account' field")
def step_impl(context):
    sing_in.enter_email_to_create_account(random_email)
    sing_in.click_create_an_account_button()
    logging.info("The random email is: '%s' ", random_email)


@then("I verify if text: {expected_text} is present in Create Account field")
def step_impl(context, expected_text):
    assert_equal(expected_text, sing_in.get_create_account_message, "The desired message is displayed")


@when("I create a new account with {mandatory} user information")
def step_impl(context, mandatory):
    # Fill all the user information

    log_in.select_gender(DataHandler().test_data('title'))
    log_in.enter_first_name(DataHandler().test_data('first_name'))
    log_in.enter_last_name(DataHandler().test_data('last_name'))
    log_in.enter_password(DataHandler().test_data('password'))
    log_in.enter_dob(DataHandler().test_data('date_of_birth'))

    if mandatory == 'all':
        log_in.enter_first_name_address(DataHandler().test_data('first_name_address'))
        log_in.enter_last_name_address(DataHandler().test_data('last_name_address'))

    log_in.enter_address(DataHandler().test_data('address_1'))
    log_in.enter_city(DataHandler().test_data('city'))
    log_in.choose_state(DataHandler().test_data('state'))
    log_in.enter_post_code(DataHandler().test_data('postal_code'))
    log_in.choose_country(DataHandler().test_data('country'))
    log_in.enter_additional_info(DataHandler().test_data('information'))
    log_in.enter_mobile_phone(DataHandler().test_data('mobile_phone'))
    log_in.enter_alias_address(DataHandler().test_data('alias_address'))

    log_in.click_register()


@then("I verify if the account was created")
def step_impl(context):
    password = DataHandler().test_data('password')
    account_name = DataHandler().test_data('first_name') + " " + DataHandler().test_data('last_name')

    context.execute_steps(u"""
        given I go to Sing In page
        given I sing in with email:{email} and pass:{password}
        when I press the Sing In button
        then I verify if the account name is:{expected_account_name}
        """.format(email=random_email, password=password, expected_account_name=account_name))
    logging.info("The account was created with email: %s and password: %s ", (random_email, password))


@Then("I sing out")
def step_impl(context):
    home.click_sing_out_button()


@then("I verify if the account name is:{expected_account_name}")
def step_impl(context, expected_account_name):
    current_account_name = home.get_account_name
    assert_equal(current_account_name, expected_account_name)
    home.click_sing_out_button()
