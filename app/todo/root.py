from fastapi import APIRouter,Depends
from app.db import get_db
from app.todo.dto import todoSchema
from sqlalchemy.orm import Session
from app.todo.controller import get_user_with_todos,get_todos_by_user
from app.todo.todoController import *
from app.user.model import User
from app.user.Is_authenticate import is_authorized

router=APIRouter(prefix="/todo")


@router.get("/usertodo/{user_id}")
def get(user_id: int, db: Session = Depends(get_db),user:User=Depends(is_authorized)):
    return get_user_with_todos(user_id,db)

@router.post("/todo")
def newTodo(body:todoSchema, db:Session=Depends(get_db), user:User=Depends(is_authorized)):
    return add_todo(body,db)

@router.get("/todo")
def getTodo(body:todoSchema, db:Session=Depends(get_db), user:User=Depends(is_authorized)):
    print(user)
    return get_todo(body,db,user)

@router.get("/filter")
def getTodoByDate(
    before: date = None,
    after: date = None,
    start: date = None,
    end: date = None,
    db: Session = Depends(get_db)
):
    return filter_todos(before,after,start,end,db)

@router.get("/todouser")
def getTodoUser(user_id: int, db:Session=Depends(get_db), user:User=Depends(is_authorized)):
    return get_todos_by_user(user_id,db)

@router.delete("/deletetodo")
def deleteTodo(todo_id: int, db: Session = Depends(get_db)):
    return delete_todo(todo_id, db)