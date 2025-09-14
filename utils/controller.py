from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.db import Base, get_db
from utils.model import User, Todo
from utils.dto import *
from utils.helper import get_user_by_username




def newUser(body:userSchema,db:Session):
    user = get_user_by_username(body.username,db)
    if user:
        raise HTTPException (401, detail={"error":"user already exist"})
    
    user= User(name=body.name, 
               email=body.email,
               mobile=body.mobile,
               username=body.username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "status":"successfully added",
        "newUser":user
    }

def get_all_user(body:userSchema, db:Session):
    users=db.query(User).all()
    return {
        "allUser":users
    }

def get_user_with_todos(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id":user.id,
        "name":user.name,
        "email":user.email,
        "username":user.username,
        "mobile":user.mobile,
        "todos": [{"title": t.title, "description": t.description,
                   "priority": t.priority, "start_date": t.start_date,
                   "end_date": t.end_date} for t in user.todos]
    }


def get_todos_by_user(user_id: int, db: Session = Depends(get_db)):
    todos = db.query(Todo).filter(Todo.user_id == user_id).all()
    if not todos:
        raise HTTPException(status_code=404, detail="No todos found for this user")
    return todos