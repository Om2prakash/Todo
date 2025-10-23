from pydantic import BaseModel
from datetime import date


class todoSchema(BaseModel):

    title :str
    description : str
    priority :str
    start_date : date
    end_date : date
    user_id : int