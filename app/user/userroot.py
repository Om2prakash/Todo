from fastapi import Request, APIRouter,Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.user.controller import  allUser
from app.user.dto import userSchema,loginDto
from app.user.authcontroller import register,login

userroute=APIRouter(prefix="/user")


@userroute.get("/user")
def getAllUser(body:userSchema, db:Session=Depends(get_db)):
    return allUser(body,db)

@userroute.post("/register")
def newUser(body:userSchema, db:Session=Depends(get_db)):
    return register(body,db)

@userroute.get("/login")
def UserLogin(body:loginDto,db:Session=Depends(get_db)):
    return login(body,db)

# @server.get("/protected")
# def protected_route(current_user: User = Depends(is_authorized)):
#     return {"message": f"Hello {current_user.username}, you are authenticated ✅"}
