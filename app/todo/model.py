from sqlalchemy import Column, Integer, String, ForeignKey, Date
from app.db import Base
# from sqlalchemy.orm import relationship


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    priority = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"))


    # owner = relationship("User", back_populates="todos")


