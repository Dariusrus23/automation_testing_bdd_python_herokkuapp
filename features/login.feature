Feature: tests for login page
  @LoginTest
  Scenario: This is a negative scenario
    Given I am on the login page
    When I insert an username "tomsmith"
    When I insert a password "SuperSecretPassword!"
    When I click on the login button
    Then The banner is displayed
    Then The message is "Your username is invalid!"