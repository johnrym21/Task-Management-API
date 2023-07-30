# Task-Management-API

This is a Flask-based API for managing tasks.

# Getting Started

# Endpoints

# Get all tasks
URL: /tasks
Method: GET

# Get task by ID
URL: /tasks/<int:task_id>
Method: GET

# Create a new task
URL: /tasks
Method: POST
Request body:

  {
    "title": "Sample Task",
    "description": "This is an example task.",
    "completed": false,
    "priority": 1,
    "due_date": "2023-08-10",
    "category": "Work"
  }

# Update an existing task
URL: /tasks/<int:task_id>
Method: PUT
Request body:

  {
    "title": "Updated Task",
    "description": "This task has been updated.",
    "completed": true,
    "priority": 2,
    "due_date": "2023-08-15",
    "category": "Personal"
  }

# Delete a task
URL: /tasks/<int:task_id>
Method: DELETE

# Get tasks sorted by highest priority
URL: /tasks/highestpriority
Method: GET

# Get tasks sorted by closest due date
URL: /tasks/closestduedate
Method: GET

# Get tasks by category
URL: /tasks/category
Method: POST
Request body:

  {
    "category": "Work"
  }

# Response Format
The API responds with JSON data in the following format:

  {
    "success": true,
    "message": "Tasks found",
    "data": 
    [
          {
            "id": 1,
            "title": "Sample Task",
            "description": "This is an example task.",
            "completed": false,
            "priority": 1,
            "due_date": "2023-08-10",
            "category": "Work"
          },
          {
            "id": 2,
            "title": "Another Task",
            "description": "This is another task.",
            "completed": true,
            "priority": 2,
            "due_date": "2023-08-15",
            "category": "Personal"
          }
        ]
    }

# Error Handling
If an error occurs, the API will respond with an error message and an appropriate status code. The success field will be set to false.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
