from fastapi import FastAPI
from settings import engine
from db_models import Base
from views import current_status, change_status

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def get_status():
    return current_status()


@app.post("/")
async def test_change_status():
    return change_status()