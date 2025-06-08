from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    writer: str


class PostResponse(PostBase):
    id: int
    created_at: datetime
    # orm_mode = True is set to enable the data model to work in ORM mode, 
    # allowing it to be used with SQLAlchemy's ORM features.
    class Config:
        orm_mode = True

class CreatePost(PostBase):
    class Config:
        orm_mode = True

