from fastapi import APIRouter,Depends
from utils.db import get_db
from utils.dto import userSchema,todoSchema
from sqlalchemy.orm import Session
from utils.controller import newUser,get_all_user,get_user_with_todos,get_todos_by_user
from utils.todoController import *


router=APIRouter(prefix="/user")

@router.get("/")
def getAllUser(body:userSchema, db:Session=Depends(get_db)):
    return get_all_user(body,db)

@router.get("/usertodo/{user_id}")
def get(user_id: int, db: Session = Depends(get_db)):
    return get_user_with_todos(user_id,db)

@router.post("/user")
def addUser(body:userSchema, db:Session=Depends(get_db)):
    return newUser(body,db)

@router.get("/todo")
def getTodo(body:todoSchema, db:Session=Depends(get_db)):
    return get_todo(body,db)

@router.post("/todo")
def newTodo(body:todoSchema, db:Session=Depends(get_db)):
    return add_todo(body,db)

@router.get("todouser")
def getTodoUser(user_id: int, db:Session=Depends(get_db)):
    return get_todos_by_user(user_id,db)