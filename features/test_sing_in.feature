@setup
Feature: Sing In

  Background: I go to Sing In page
    Given I load the website
    Given I go to Sing In page

  Scenario Outline: Sing in with invalid email and password

    When I sing in with email:<Username> and pass: <Password>
    When I press the Sing In button
    Then Verify if the expected error message:Invalid email address. is displayed in Sing In field

    Examples:
          |Username|Password|
          |ruxi|Ruxandra11|
          |dsjds|dads|

  Scenario: Sing in with valid email and invalid password

    When I sing in with email:ruxi.ierima@gmail.com and pass:ffwfwfwfw
    When I press the Sing In button
    Then Verify if the expected error message:Authentication failed. is displayed in Sing In field

  Scenario: Sing in with valid email and valid password

     When I sing in with email:ruxi.ierima@gmail.com and pass:Ruxandra11
     When I press the Sing In button
     Then Verify if the account name is:Ruxandra Ierima
     Then I sing out
