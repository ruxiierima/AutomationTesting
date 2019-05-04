from behave import *
from behave import step

from page_object.sing_in import sing_in, SingIn
from page_object.home import home
from utilis.driver import web_driver

@given("I navigate to home page")
def step(context):
    web_driver.get_driver()
    web_driver.load_website()

@when("I sing in with email:{email} and pass:{password}")
def step_impl(context,email,password):
    step.emailData = [email]
    step.passData = [password]

    sing_in = home.click_sing_in_button()
    sing_in.enter_email(email)
    sing_in.enter_password(password)


@when("I press the Sing In button")
def step_impl(context):
    sing_in.click_sing_in_button()


@then("Verify if an error message is displayed")
def step_impl(context):
    assert True==SingIn.SingInAuthentication().is_error_message_present(),"The error message is displayed"