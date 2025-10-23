from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import Base, get_db
from app.todo.model import  Todo
from app.user.model import  User


def get_user_with_todos(user_id: int, db: Session,user:User):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id":user.id,
        "name":user.name,
        "email":user.email,
        "username":user.username,
        "todos": [{"title": t.title, "description": t.description,
                   "priority": t.priority, "start_date": t.start_date,
                   "end_date": t.end_date} for t in user.todos]
    }


def get_todos_by_user(user_id: int, db: Session = Depends(get_db)):
    todos = db.query(Todo).filter(Todo.user_id == user_id).all()
    if not todos:
        raise HTTPException(status_code=404, detail="No todos found for this user")
    return todos