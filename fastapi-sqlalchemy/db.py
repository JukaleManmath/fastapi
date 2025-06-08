from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_URL = 'postgresql://manmathjukale:Hruta%40005@localhost/fastapi'

engine = create_engine(DB_URL)

# session for performing the database operations
SessionLocal = sessionmaker(autocommit= False ,autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
