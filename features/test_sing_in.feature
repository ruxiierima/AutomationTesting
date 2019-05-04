  Feature: Sing In

    Scenario: Sing in with invalid email and password

      Given I navigate to home page
      When I sing in with email:ruxi and pass: 1234
      When I press the Sing In button
      Then Verify if an error message is displayed


