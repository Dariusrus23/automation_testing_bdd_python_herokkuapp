Feature: tests for login page
  @LoginFail
  Scenario: This is a negative scenario with incorrect username and password
    Given I am on the login page
    When I insert an username1 "darius@gmail.com"
    When I insert a password2 "Darius!1"
    When I click on the login button1
    Then The banner is displayed1
    Then The message is "Your username is invalid!"

  @LoginOutline
  Scenario Outline: This is scenario with multiple parameters
    Given I am on the login page
    When I insert an username "<email>"
    When I insert a password "<password>"
    When I click on the login button
    Then The banner is displayed
    Then The message is displayd "You logged into a secure area!"

  Examples:
  | email           | password            |
  | admin@gmail.com | 12345               |
  | dasoidnm1       | 12312321321         |
  | oindasid1       | 13kmndaso0in13123ds |
  | tomsmith        | SuperSecretPassword!|
