from pydantic import BaseModel

class userSchema(BaseModel):

    name:str
    email:str
    username:str
    password:str

class loginDto(BaseModel):

    username:str
    password:str

