Feature: Calculator
  As a user
  I want to perform basic arithmetic operations
  ....

  Background:
    Given I have a calculator

  Scenario: Add two positive numbers
    When I add 1 and 2
    Then the result should be 3
    And the result should be greater than 0

  Scenario: Subtraction of two numbers
    When I subtract 1 from 2
    Then the result should be 1

  Scenario Outline: Addition of two numbers
    When I add <a> and <b>
    Then the result should be <result>

    Examples:
      | a  | b  | result |
      | -1 |  2 |  1 |
      | -1 | -2 | -3 |
      |  0 |  0 |  0 |

  Scenario: Addition with table
    When I perform the following additions:
      | a  | b  | result |
      | -1 |  2 |  1 |
      | -1 | -2 | -3 |
      |  0 |  0 |  0 |
    Then all results should be correct