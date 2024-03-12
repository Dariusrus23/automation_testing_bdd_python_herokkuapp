Feature: tests for login page

  Background:
    Given I am on the login page

  @LoginFail
  Scenario: This is a negative scenario with incorrect username and password
    When I insert an username "darius@gmail.com"
    When I insert a password "Darius!1"
    When I click on the login button
    Then The banner is displayed
    Then The message is "Your username is invalid!"

  @LoginOutline
  Scenario Outline: This is scenario with multiple parameters
    When I insert an username "<email>"
    When I insert a password "<password>"
    When I click on the login button
    Then The banner is displayed
    Then The message is displayed
    Then The message is "<message>"

  Examples:
    | email           | password             | message                        |
    | admin@gmail.com | 12345                | Your username is invalid!      |
    | dasoidnm1       | 12312321321          | Your username is invalid!      |
    | oindasid1       | 13kmndaso0in13123ds  | Your username is invalid!      |
    | tomsmith        | SuperSecretPassword! | You logged into a secure area! |
