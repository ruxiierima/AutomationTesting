# Created by ierima at 7/2/2019

@setup
Feature: Sort search results
"""

When a user perform a product search
and choose a sort method the results should
be displayed by chosen method and should be relevant
"""

  Scenario Outline: Search a product
    Given I load the website
    When I search product 'dress'
    And I sort results by <sort_method>
    Then Results should be displayed by <sort_method>
    And All the results should be relevant for search 'dress'

    Examples:
      | sort_method |
      | Price: Lowest first|
      | Price: Highest first|
