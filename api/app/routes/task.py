from app.core.database import get_db
from app.cruds import task as task_cruds
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=list[TaskRead])
def list_tasks(session: Session = Depends(get_db)):
    return task_cruds.fetch_tasks(session)


@router.post("/", response_model=TaskRead)
def create_task(task: TaskCreate, session: Session = Depends(get_db)):
    return task_cruds.create_task(session, task=task)


@router.patch("/{id}", response_model=TaskRead)
def update_task(id: str, task: TaskUpdate, session: Session = Depends(get_db)):
    original = task_cruds.fetch_task(session, id)
    if original is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task_cruds.update_task(session, task=task, original=original)


@router.delete("/{id}")
def delete_task(id: str, session: Session = Depends(get_db)):
    original = task_cruds.fetch_task(session, id)
    if original is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task_cruds.delete_task(session, original=original)
