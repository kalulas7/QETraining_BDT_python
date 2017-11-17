Feature: API
  test configuration
  Scenario: scenario
    Given I have connection to "http://todo.ly"
    When I send GET
    Then I'll receive status code 200