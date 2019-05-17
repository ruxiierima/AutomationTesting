# Created by ierima at 5/10/2019

  Feature: Create new Account

     Background: I go to Sing In page
      Given I load the website
      Given I go to Sing In page

    Scenario: Create an account with valid email
      Then I verify if text: Please enter your email address to create an account. is present in Create Account field
      When Create a new account with email: ruxi.ierima@gmail.com
      And Create new account


