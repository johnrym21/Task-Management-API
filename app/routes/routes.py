import re
from flask import request, Blueprint
from app.service.tasks import get_all_tasks, create_task, get_task_by_id, update_task, delete_task, get_tasks_by_highest_priority, get_tasks_by_closest_due_date, get_tasks_by_category
from app.responses.custom_response import custom_response
from datetime import datetime


tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('/tasks', methods=['GET'])
def get_all_tasks_route():
    try:
        tasks = get_all_tasks()
        if not tasks:
            return custom_response(success=True, message="No tasks found", data=[])

        return custom_response(success=True, message="Tasks found", data=[task.serialize() for task in tasks])
    
    except Exception as e:
        return custom_response(success=False, message="An error occurred while fetching tasks", data=e, status_code=500)


@tasks_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id_route(task_id):
    try:
        task = get_task_by_id(task_id)
        if not task:
            return custom_response(success=False, message="Task not found", data=None, status_code=404)

        return custom_response(success=True, message="Task found", data=task.serialize())

    except Exception as e:
        return custom_response(success=False, message="An error occurred while fetching the task", data=None, status_code=500)



@tasks_bp.route('/tasks', methods=['POST'])
def create_task_route():
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        completed = data.get('completed')
        priority = data.get('priority')
        due_date = data.get('due_date')
        category = data.get('category')

        if not title or not description:
            return custom_response(success=False, message="Title and description are required fields", data=None, status_code=400)
        
        if priority is not None and (not isinstance(priority, int) or priority <= 0):
            return custom_response(success=False, message="Priority must be a positive integer", data=None, status_code=400)
        
        if completed is not isinstance(priority, bool):
            return custom_response(success=False, message="Completed must be a boolean (true or false)", data=None, status_code=400)

        new_task = create_task(title, description, completed, priority, due_date, category)
        return custom_response(success=True, message="Task created successfully", data=new_task.serialize(), status_code=201)

    except Exception as e:
        return custom_response(success=False, message="An error occurred while creating the task", data=None, status_code=500)



@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task_route(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return custom_response(success=False, message="Task not found", data=None, status_code=404)

    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        completed = data.get('completed')
        priority = data.get('priority')
        due_date = data.get('due_date')
        category = data.get('category')

        if not title or not description:
            return custom_response(success=False, message="Title and description are required fields", data=None, status_code=400)
        
        if priority is not None and not isinstance(priority, int) and priority <= 0:
            return custom_response(success=False, message="Priority must be a positive integer", data=None, status_code=400)
        
        if completed is not isinstance(priority, bool):
            return custom_response(success=False, message="Completed must be a boolean (true or false)", data=None, status_code=400)

        updated_task = update_task(task, title, description, completed, priority, due_date, category)
        return custom_response(success=True, message="Task updated successfully", data=updated_task.serialize())

    except Exception as e:
        return custom_response(success=False, message="An error occurred while updating the task", data=None, status_code=500)


@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task_route(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return custom_response(success=False, message="Task not found", data=None, status_code=404)

    try:
        delete_task(task)
        return custom_response(success=True, message="Task deleted successfully", data=None)

    except Exception as e:
        return custom_response(success=False, message="An error occurred while deleting the task", data=None, status_code=500)
    
@tasks_bp.route('/tasks/highestpriority', methods=['GET'])
def get_tasks_by_highest_priority_route():
    try:
        tasks = get_tasks_by_highest_priority()
        if not tasks:
            return custom_response(success=True, message="No tasks found", data=[])

        return custom_response(success=True, message="Tasks sorted by highest priority", data=[task.serialize() for task in tasks])

    except Exception as e:
        return custom_response(success=False, message="An error occurred while fetching tasks", data=e, status_code=500)

@tasks_bp.route('/tasks/closestduedate', methods=['GET'])
def get_tasks_by_closest_due_date_route():
    try:
        tasks = get_tasks_by_closest_due_date()
        if not tasks:
            return custom_response(success=True, message="No tasks found", data=[])

        return custom_response(success=True, message="Tasks sorted by closest due date", data=[task.serialize() for task in tasks])

    except Exception as e:
        return custom_response(success=False, message="An error occurred while fetching tasks", data=e, status_code=500)
    
@tasks_bp.route('/tasks/category', methods=['POST'])
def get_tasks_by_category_route():
    try:
        data = request.get_json()
        category = data.get('category')
        if not category:
            return custom_response(success=False, message="Category is required", data=None, status_code=400)

        tasks = get_tasks_by_category(category)
        if not tasks:
            return custom_response(success=True, message=f"No tasks found for the category '{category}'", data=[])

        return custom_response(success=True, message=f"Tasks for category '{category}'", data=[task.serialize() for task in tasks])

    except Exception as e:
        return custom_response(success=False, message="An error occurred while fetching tasks", data=e, status_code=500)