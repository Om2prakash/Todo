# from datetime import datetime,timedelta, timezone
import  jwt
from fastapi import HTTPException,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.user.dto import userSchema,loginDto
from sqlalchemy.orm import Session
from app.user.helper import get_user_by_username,get_password_hass,get_verify_password
from app.user.model import User

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def register(body:userSchema  , db:Session):
    currentUser = get_user_by_username(body.username,db)
    if currentUser:
        raise HTTPException(401,detail={"message":"user all ready exist"})
    hp = get_password_hass(body.password)
    newUser= User(name=body.name,email=body.email,username=body.username,password=hp)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return {
        "status":"added succesfully",
        "user":newUser
        }

def login(body:loginDto, db:Session):
    currentUser=get_user_by_username(body.username, db)
    if not currentUser:
        raise HTTPException(401, detail={"error":"user already exist"})
    verifyPassword= get_verify_password(body.password,currentUser.password)   
    if not verifyPassword:
        raise HTTPException(401,detail={"error":"password incorrect"})
    token= jwt.encode({"username":currentUser.username},SECRET_KEY,algorithm=ALGORITHM)
    return{
        "status":"succesfully login",
        "detail":currentUser,
        "token":token
    }
