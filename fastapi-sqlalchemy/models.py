from db import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


# table structure to be created in the database
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    writer = Column(String, nullable=False, server_default="Unknown")
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


