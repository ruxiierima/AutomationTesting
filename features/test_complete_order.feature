# Created by ierima at 6/23/2019

@setup
Feature: Complete order
"""User should be able to complete an order
"""
    Background:
    Given I load the website
    And I go to Sing In page
    And I log in with email:ruxi.ierima@gmail.com and pass:Ruxandra11

"""Delivery address should be displayed
when user want to complete an order
"""
#    Scenario: Check delivery address
#    Given I add product 'Faded Short Sleeve T-shirts,Printed Summer Dress' to the cart
#    When I go to delivery address
#    Then I check delivery address for account: 'ruxi.ierima@gmail.com'

  """User should be able to pay for an order via
  bank transfer or via check
  """
  Scenario Outline: Payment methods
    Given I add product 'Faded Short Sleeve T-shirts,Blouse' to the cart
    When I proceed to checkout
    And I choose to pay via  <Paymethod>
    Then The confirmation of the <Paymethod> payment should be displayed
    And I should be able to submit my order

    Examples:
      | Paymethod |
      | bank      |
      | check     |
