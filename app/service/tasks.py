from app.models.tasks import Tasks
from app import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import asc

def get_all_tasks():
    try:
        return Tasks.query.all()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e

def create_task(title, description, completed, priority=None, due_date=None, category=None):
    try:
        new_task = Tasks(title=title, description=description, completed=completed,
                         priority=priority, due_date=due_date, category=category)
        db.session.add(new_task)
        db.session.commit()
        return new_task
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e

def get_task_by_id(task_id):
    try:
        return Tasks.query.get(task_id)
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e

def update_task(task, title, description, completed, priority=None, due_date=None, category=None):
    try:
        task.title = title
        task.description = description
        task.completed = completed
        task.priority = priority
        task.due_date = due_date
        task.category = category
        db.session.commit()
        return task
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e

def delete_task(task):
    try:
        db.session.delete(task)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e

def get_tasks_by_highest_priority():
    try:
        return Tasks.query.order_by(Tasks.priority.desc()).all()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e
    
def get_tasks_by_closest_due_date():
    try:
        return Tasks.query.order_by(asc(Tasks.due_date)).all()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e
    
def get_tasks_by_closest_due_date():
    try:
        return Tasks.query.order_by(asc(Tasks.due_date)).all()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e
    
def get_tasks_by_category(category):
    try:
        return Tasks.query.filter(Tasks.category.ilike(category)).all()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e