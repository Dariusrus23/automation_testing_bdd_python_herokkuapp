Feature: tests for login page
  @LoginFail
  Scenario: This is a negative scenario with incorrect username and password
    Given I am on the login page
    When I insert an username "darius@gmail.com"
    When I insert a password "Darius!1"
    When I click on the login button
    Then The banner is displayed
   # Then The message is "Your username is invalid!"

  @LoginTrue
  Scenario: This is a positive scenario
    Given I on the login page1
    When I insert an username1 "tomsmith"
    When I insert a password1 "SuperSecretPassword!"
    When I click on the login button1
    Then The banner is displayed1
    #Then The displayed message is "You logged into a secure area!"

