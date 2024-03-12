Feature: this test suite tests search feature on Emag.ro website

@EmagSearch
Scenario: This scenario will test the search feature for specific keyword
  Given I am on the home page
  When I click on the search box
  When I enter the keyword "iphone"
  When I click the magnifier icon
  Then "iphone" keyword is in title phrasing element
