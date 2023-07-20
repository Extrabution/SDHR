from pydantic import BaseModel

class History(BaseModel):
    start_date: str
    end_date: str
    status: str