# Created by ierima at 5/10/2019

@setup
Feature: Create new Account
"""
After a new account was created the
home page should display the user name( First Name Last Name)
at the top-right corner of the page
"""

   Background: I navigate to Sing In page
    Given I load the website
    Given I go to Sing In page
    Then I verify if text: Please enter your email address to create an account. is present in Create Account field

  """
  An account can be created even if only
  the mandatory information in the registration form are filled in
  """
  Scenario: Create an account with valid email

    Given I insert random email into 'Create account' field
    When I create a new account with mandatory user information
    Then I sing out
    Then I verify if the account was created


