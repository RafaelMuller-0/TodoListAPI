from fastapi import Depends, FastAPI, HTTPException
from typing import Annotated

from psycopg.types import none

from database import get_connection
from sqlalchemy import text, Connection, select
from sqlalchemy.orm import Session
from schemas import TaskCreate, TaskResponse
from database import get_session
from models import Task

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API funcionando"}

@app.get("/db-test")
def test_db(con: Annotated[Connection,Depends(get_connection)]):
    test = con.execute(text("select 1")).scalar()
    return test

@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate, session: Annotated[Session,Depends(get_session)]):
    new_task = Task(title=task.title)
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task

@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks(session: Annotated[Session,Depends(get_session)]):
    tasks = session.scalars(select(Task).order_by(Task.id)).all()
    return tasks

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, session: Annotated[Session,Depends(get_session)]):
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task