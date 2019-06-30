# Created by ierima at 5/10/2019

@setup
Feature: Create new account
"""
After a new account was created the
home page should display the user name( First Name Last Name)
at the top-right corner of the page
"""
   Background: I navigate to Sing In page
     Given I load the website
     And I go to Sing In page
     Then Create Account field should be displayed

  """
  An account can be created just
  with mandatory information
  """
  Scenario: Create an account with mandatory information

    Given I insert 'random_email' into Create account field
    When I create a new account for 'random_email' with mandatory user information
    Then I verify if the account 'random_email' was created


