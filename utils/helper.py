from utils.model import User
from sqlalchemy.orm import Session




def get_user_by_username(username:str , db:Session):
    user= db.query(User).filter(User.username== username).first()
    return user