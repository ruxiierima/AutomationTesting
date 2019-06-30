from behave import *
from nose.tools import assert_equal
from page_object.sing_in import sing_in
from page_object.log_in import log_in
from page_object.home import home
from utils import values
from utils.driver import web_driver
from utils.data_handler import DataHandler
import logging

random_email = DataHandler().generate_random_emails()


@given("I load the website")
def step(context):
    web_driver.load_website()


@given("I go to Sing In page")
def step_impl(context):
    if home.already_sing_in:
        home.click_sing_out_button()
    home.click_sing_in_button()


@given("I sing in with email:{email} and pass:{password}")
def step_impl(context, email, password):
    sing_in.enter_email(email)
    sing_in.enter_password(password)

@given("I log in with email:{desired_email} and pass:{desired_password}")
def step_impl(context,desired_email,desired_password):
    context.execute_steps(u"""
            given I sing in with email:{email} and pass:{password}
            when I press the Sing In button
            """.format(email=desired_email, password=desired_password))

@when("I press the Sing In button")
def step_impl(context):
    sing_in.click_sing_in_button()


@then("I check if the expected error message:{expected_message} is displayed in Sing In field")
def step_impl(context, expected_message):
    assert_equal(expected_message, sing_in.get_errot_message, "The error message is displayed")


@given("I insert '{desired_email}' into Create account field")
def step_impl(context, desired_email):
    if desired_email == 'random_email':
        desired_email = random_email

    sing_in.enter_email_to_create_account(desired_email)
    sing_in.click_create_an_account_button()
    logging.info("The email is: '%s' ", desired_email)


@then("Create Account field should be displayed")
def step_impl(context):
    assert_equal(values.CREATE_NEW_ACCOUNT_TEXT, sing_in.get_create_account_message, "The desired message is displayed")


@when("I create a new account for '{desired_email}' with {mandatory} user information")
def step_impl(context, mandatory, desired_email):

    # Fill all the user information
    log_in.select_gender(DataHandler().test_data('title',desired_email))
    log_in.enter_first_name(DataHandler().test_data('first_name',desired_email))
    log_in.enter_last_name(DataHandler().test_data('last_name',desired_email))
    log_in.enter_password(DataHandler().test_data('password',desired_email))
    log_in.enter_dob(DataHandler().test_data('date_of_birth',desired_email))

    if mandatory == 'all':
        log_in.enter_first_name_address(DataHandler().test_data('first_name',desired_email))
        log_in.enter_last_name_address(DataHandler().test_data('last_name',desired_email))

    log_in.enter_address(DataHandler().test_data('address_1',desired_email))
    log_in.enter_city(DataHandler().test_data('city',desired_email))
    log_in.choose_state(DataHandler().test_data('state',desired_email))
    log_in.enter_post_code(DataHandler().test_data('postal_code',desired_email))
    log_in.choose_country(DataHandler().test_data('country',desired_email))
    log_in.enter_additional_info(DataHandler().test_data('information',desired_email))
    log_in.enter_mobile_phone(DataHandler().test_data('mobile_phone',desired_email))
    log_in.enter_alias_address(DataHandler().test_data('alias_address',desired_email))

    log_in.click_register()


@then("I verify if the account '{email}' was created")
def step_impl(context,email):
    password = DataHandler().test_data('password', email)
    account_name = DataHandler().test_data('first_name', email) + " " + DataHandler().test_data('last_name', email)

    context.execute_steps(u"""
        given I sing out
        given I go to Sing In page
        given I sing in with email:{email} and pass:{password}
        when I press the Sing In button
        then I verify if the account name is:{expected_account_name}
        """.format(email=random_email, password=password, expected_account_name=account_name))
    logging.info("The account was created with email: %s and password: %s ", (random_email, password))


@given("I sing out")
def step_impl(context):
    home.click_sing_out_button()


@then("I verify if the account name is:{expected_account_name}")
def step_impl(context, expected_account_name):
    current_account_name = home.get_account_name
    assert_equal(current_account_name, expected_account_name)
