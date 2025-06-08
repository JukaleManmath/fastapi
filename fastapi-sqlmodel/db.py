from sqlmodel import SQLModel, Session, create_engine

DB_URL = "postgresql://<username>:<password>@localhost:5432/SQLModelTest"

engine = create_engine(DB_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
