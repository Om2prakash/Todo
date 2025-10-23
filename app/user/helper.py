from sqlalchemy.orm import Session
from app.user.model import User
from passlib.context import CryptContext


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(username:str , db:Session):
    user= db.query(User).filter(User.username== username).first()
    print(f"[DEBUG] Using DB Session ID: {id(db)}")
    return user

def get_password_hass(password):
    return pwd_context.hash(password)

def get_verify_password(plain_password , hass_password):
    return pwd_context.verify(plain_password,hass_password)

