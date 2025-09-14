from fastapi import FastAPI 
from utils.root import router
from utils.db import Base,intilize

Base.metadata.create_all(intilize)

server=FastAPI()
server.include_router(router)

