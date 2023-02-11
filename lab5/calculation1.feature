Feature: Test calculations

  Scenario Outline: Count discriminant
    Given I have the numbers <num1>, <num2> and <num3>
    When I count discriminant
    Then I expect the result to be <result>

    Examples:
      | num1 | num2 | num3 | result |
      |  1   |  1  |  1   |  -3   |
      |  0.25   |  0  |  -1  |  1  |
      |  0   |  10  |  -1000  |  100  |