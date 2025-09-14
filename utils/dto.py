from pydantic import BaseModel
from datetime import date

class userSchema(BaseModel):
    name :str
    email : str
    username :str
    mobile : int

class todoSchema(BaseModel):

    title :str
    description : str
    priority :str
    start_date : date
    end_date : date
    user_id : int