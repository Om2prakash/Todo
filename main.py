from fastapi import FastAPI 
from app.todo.root import router
from app.user.userroot import userroute
from app.db import Base,intilize

Base.metadata.create_all(intilize)

server=FastAPI()
server.include_router(router)
server.include_router(userroute)


