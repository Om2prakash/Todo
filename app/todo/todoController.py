from app.todo.dto import todoSchema
from sqlalchemy.orm import Session
from app.todo.model import Todo
from app.user.model import User
from fastapi import HTTPException, Depends, BackgroundTasks
from datetime import date,datetime,time
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler  # runs tasks in the background
from apscheduler.triggers.cron import CronTrigger  # allows us to specify a recurring time for execution
from apscheduler.triggers.interval import IntervalTrigger
from app.db import localSession
from time import sleep
from app.todo.dto import todoSchema


# scheduler =BackgroundScheduler()

# def engageTime():
#     sleep(5)
#     print("heyyy...")

# trigger= IntervalTrigger(seconds=3,start_date=datetime.now())
# scheduler.add_job(engageTime, trigger)
# scheduler.start()


def get_todo(body:todoSchema, db:Session,user:User):
    # engageTime()
    todoList =db.query(Todo).order_by(Todo.title.asc()).all()
    return{
        "List":todoList
    }

def filter_todos(
        db:Session ,user:User,
    before: date = None,
    after: date = None,
    start: date = None,
    end: date = None,
   ):
    query = db.query(Todo)

    # Case 1: Before a given date
    if before:
        query = query.filter(Todo.start_date < before)

    # Case 2: After a given date
    if after:
        query = query.filter(Todo.start_date > after)

    # Case 3: Between two dates
    if start and end:
        query = query.filter(Todo.start_date.between(start, end))

    todos = query.all()

    if not todos:
        raise HTTPException(status_code=404, detail="No todos found with given filter")

    return todos

def add_todo(body:todoSchema, db:Session,user:User):
    todo= Todo(**body.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "status":"succesfully added todo",
        "todo":todo
    }

def delete_todo(todo_id: int, db: Session, user:User ):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(todo)
    db.commit()
    return {"message": f"Todo {todo_id} deleted successfully"}
