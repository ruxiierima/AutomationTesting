# Created by ierima at 5/24/2019

@setup
Feature: Shopping products
"""Product details from cart summary should
be the same as those shown on the home page
"""

   Background: I go to home page
    Given I load the website

  Scenario: Submit an order
    Given I add 7 products to the cart
    Then I check if the expected quantity: '7' added to the cart is correct
    When I click on check out button
    Then I check if all product details from cart summary are the same with products from the cart

