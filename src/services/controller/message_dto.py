from pydantic import BaseModel


class Message(BaseModel):
    datetime: str
    payload: int


