@setup
Feature: Sing In

  Background: I navigate to Sing In page
    Given I go to Sing In page

  """
  When a user want to login with an INVALID email/password
  should NOT be able to login successfully and an error message should
  appear:'Invalid email address.'
  """
  Scenario Outline: Sing in with invalid email and password

    Given I sing in with email:<Username> and pass: <Password>
    When I press the Sing In button
    Then I check if the expected error message:Invalid email address. is displayed in Sing In field

    Examples:
          |Username|Password|
          |ruxi|Ruxandra11|
          |dsjds|dads|

  """
  When a user want to login with an VALID email and a WRONG password
  should NOT be able to login successfully and an error message should
  appear:'Authentication failed'
  """
  Scenario: Sing in with valid email and invalid password

    Given I sing in with email:ruxi.ierima@gmail.com and pass:ffwfwfwfw
    When I press the Sing In button
    Then I check if the expected error message:Authentication failed. is displayed in Sing In field

  """
  When a user want to login with an valid email/password
  should be able to login successfully and the account
  name should be the user full name.
  """
  Scenario: Sing in with valid email and valid password

     Given I sing in with email:ruxi.ierima@gmail.com and pass:Ruxandra11
     When I press the Sing In button
     Then I verify if the account name is:Ruxandra Ierima
