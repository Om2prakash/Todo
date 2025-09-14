from utils.dto import todoSchema
from sqlalchemy.orm import Session
from fastapi import Depends
from utils.model import Todo



def get_todo(body:todoSchema, db:Session):
    todoList =db.query(Todo).all()
    return{
        "List":todoList
    }

def add_todo(body:todoSchema, db:Session):
    todo= Todo(**body.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "status":"succesfully added todo",
        "todo":todo
    }
