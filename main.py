from fastapi import Depends, FastAPI
from typing import Annotated
from database import get_connection
from sqlalchemy import text, Connection
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API funcionando"}

@app.get("/db-test")
def test_db(con: Annotated[Connection,Depends(get_connection)]):
    test = con.execute(text("select 1")).scalar()
    return test

@app.post("/tasks")
with Session(engine) as session:
