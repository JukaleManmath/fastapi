from sqlmodel import SQLModel , Field
from datetime import datetime
from typing import Optional

class PostBase(SQLModel):
    title: str
    content: str
    writer: str

class Post(PostBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    published: bool = Field(default=True)


class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int 
    created_at: datetime
    published: bool 