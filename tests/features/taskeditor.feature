Feature: Edit tasks
  In order to track my to do list
  As a worker
  I want to create and update my tasks

  Scenario: Create a new task
    Given that I have a task editor
    When I enter "Task 1" in the task name
    And I press the OK button
    Then I see "Task 1"