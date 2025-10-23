from app.user.dto import *
from app.user.model import *
from sqlalchemy.orm import Session
from fastapi import Request, Depends, HTTPException
from app.db import *
import jwt
from app.user.authcontroller import SECRET_KEY,ALGORITHM,get_user_by_username

def is_authorized(req:Request, database:Session = Depends(get_db)):
    token = req.headers.get("authorization")
    if not token:
        raise HTTPException(status_code=401, detail={"error":"you are unauthorized"})
    token =token.split(" ")[-1]

    print(token)
    data=jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
    print(data)
    if not data.get("username"):
        raise HTTPException(status_code=401,detail={"error":"you are unauthorized"})
    user = get_user_by_username(data.get("username"),database)
    if not user:
        raise HTTPException(status_code=401,detail={"error":"you are unauthorized"})
    return user