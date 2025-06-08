from fastapi import FastAPI
from routes import router
from db import engine
import models

app = FastAPI()

# DO NOT NEED AS WE ARE USING ALEMBIC MIGRATIONS
# for tables from models.py to be created in the database
# models.Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/post", tags=['Posts'])

