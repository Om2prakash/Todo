from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine

url_db= "sqlite:///./Database.db"

Base=declarative_base()
intilize = create_engine(url_db)

localSession = sessionmaker(bind=intilize,autoflush=False )

def get_db():

    try:
        db = localSession()
        yield db
    finally :
        db.close()