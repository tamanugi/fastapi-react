from app.core.database import get_db
from app.cruds import task as task_cruds
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=list[TaskRead])
def list_tasks(session: Session = Depends(get_db)):
    return task_cruds.fetch_tasks(session)


@router.post("/", response_model=TaskRead)
def create_task(task: TaskCreate):
    pass


@router.patch("/{id}", response_model=TaskRead)
def update_task(id: str, task: TaskUpdate):
    pass


@router.delete("/{id}")
def delete_task(id: str):
    pass
