# SQLModel and SQLAlchemy Migration Guide with Alembic (FastAPI + PostgreSQL)

This document walks through how to build a FastAPI app using SQLAlchemy, migrate it using Alembic, and then convert the same project to SQLModel with Alembic.

---

## 🧱 Part 1: Start with SQLAlchemy + Alembic

### 📦 `requirements.txt`

```
fastapi
sqlalchemy
alembic
psycopg2-binary
uvicorn
pydantic
```

### 🗂️ Folder Structure

```
project/
├── app/
│   ├── models.py
│   ├── schema.py
│   ├── db.py
│   ├── routes.py
│   └── main.py
├── alembic/
│   ├── versions/
│   └── env.py
├── alembic.ini
└── requirements.txt
```

### `models.py`

```python
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text
from app.db import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
```

### `schema.py`

```python
from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
```

### `db.py`

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@localhost:5432/yourdb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 🔁 Alembic Setup for SQLAlchemy

```bash
alembic init alembic
```

Update `alembic/env.py`:

```python
from app.models import Base

target_metadata = Base.metadata
```

Then run migrations:

```bash
alembic revision --autogenerate -m "create posts table"
alembic upgrade head
```

---

## 🔁 Part 2: Convert SQLAlchemy Project to SQLModel

### 🔄 Step-by-step Migration

1. Replace `Base = declarative_base()` with SQLModel
2. Remove `Column()` syntax — use `Field()` from SQLModel
3. Delete `schema.py`; use Pydantic + ORM in one SQLModel class
4. Change query patterns from `.query(...)` to `session.exec(select(...))`
5. Update `alembic/env.py`:

```python
from app.models import SQLModel

target_metadata = SQLModel.metadata
```

---

## ✅ Part 3: SQLModel + Alembic Starter Template

### 🗂 Folder Structure

```
project/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── db.py
│   └── routes.py
├── alembic/
│   ├── versions/
│   └── env.py
├── alembic.ini
└── requirements.txt
```

### `requirements.txt`

```
fastapi
sqlmodel
uvicorn
psycopg2-binary
alembic
```

### `models.py`

```python
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    published: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
```

### `db.py`

```python
from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://user:password@localhost:5432/yourdb"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
```

### `main.py`

```python
from fastapi import FastAPI
from app.db import create_db_and_tables
from app.routes import router as post_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(post_router)
```

### `routes.py`

```python
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.db import get_session
from app.models import Post

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", response_model=Post)
def create_post(post: Post, session: Session = Depends(get_session)):
    session.add(post)
    session.commit()
    session.refresh(post)
    return post

@router.get("/", response_model=list[Post])
def get_posts(session: Session = Depends(get_session)):
    return session.exec(select(Post)).all()
```

---

## 📌 Alembic & PostgreSQL Migration Tips

### 🧠 Best Practices

* Use `alembic revision --autogenerate -m "message"` for clean diffs
* Review each migration file before running
* Use `alembic upgrade head` after each schema change
* Automate migration runs in CI/CD for production
* Split large changes into small revisions

### 🛠 Alembic Commands

```bash
alembic init alembic
alembic revision --autogenerate -m "create posts table"
alembic upgrade head
alembic downgrade -1
```

---

Now you have a clear guide:

* Start with SQLAlchemy and Alembic
* Migrate and manage PostgreSQL schemas
* Convert to SQLModel for cleaner, unified code
* Maintain migrations using Alembic with either approach
