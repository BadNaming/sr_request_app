from fastapi import FastAPI
from sqlalchemy import create_engine
from db_models import Base
from views import index

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return index()