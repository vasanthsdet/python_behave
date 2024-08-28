Feature: API Endpoint Testing

  Scenario: Validate the response of a GET request
    Given the API endpoint "https://api.agify.io/?name=meelad"
    When I send a GET request
    Then the response status code should be 200
    And the response body should contain "count"
