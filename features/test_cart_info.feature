# Created by ierima at 5/24/2019

@setup
Feature: Cart Info
"""Product details from cart summary should
be the same as those shown on the home page
"""

   Background: I go to home page
    Given I load the website

  Scenario: Check cart information
    Given I add 7 products to the cart
    When I click on check out button
    Then I check if all product details from the cart are the same with products from cart summary
    And I check if the expected quantity: '7' added to the cart is correct
    And I check if total amount is correct

