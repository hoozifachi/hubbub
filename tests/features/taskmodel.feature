Feature: Store tasks
  In order to track my to do list
  As a worker 
  I need to store my tasks of retrieval later

  Scenario: Store a new task
    Given that I have a task object with the name "Task 1"
    When I commit the session
    Then I find "Task 1" in the database
