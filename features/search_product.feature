Feature: this feature will contain only tests related to search
  @searchitem
  Scenario: I an on the main page and search for a product
    Given I am on the main page
    When I click on the search button
    When I enter this name product "Fals tratat de manipulare"
    When I click the magnifier
    Then The product "Fals tratat de manipulare"

