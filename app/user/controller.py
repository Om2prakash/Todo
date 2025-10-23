from app.user.dto import userSchema
from sqlalchemy.orm import Session
from app.user.model import User
from app.user.helper import get_user_by_username
from fastapi import HTTPException


def allUser(body:userSchema, db:Session):
    alluser=db.query(User).all()
    return {
        "userData":"data of users",
        "data":alluser
    }

def deleteUser(body:userSchema, db:Session):

    currentUser=get_user_by_username(body.username, db)
    if not currentUser:
        raise HTTPException(401, detail={"error":"user does not exist"})
    db.delete(currentUser)
    db.commit()

    return {"message": f"User '{body.username}' deleted successfully"}

def updateUser(body: userSchema, db: Session):
    currentUser = get_user_by_username(body.username, db)
    if not currentUser:
        raise HTTPException(status_code=404, detail={"error": "User not found"})

    if body.email:
        currentUser.email = body.email
    if body.name:
        currentUser.name = body.name
    if body.password:
        from app.user.helper import get_password_hass   # avoid circular import
        currentUser.password = get_password_hass(body.password)

    db.commit()
    db.refresh(currentUser)

    return {"message": f"User '{body.username}' updated successfully", "user": {
        "username": currentUser.username,
        "email": currentUser.email,
        "age": currentUser.name
    }}
    



