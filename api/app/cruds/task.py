from app.models.task import TaskModel
from app.schemas.task import TaskCreate, TaskUpdate
from sqlalchemy.orm import Session


def fetch_task(session: Session, id: str) -> TaskModel | None:
    return session.query(TaskModel).get(id)


def fetch_tasks(session: Session) -> list[TaskModel]:
    return session.query(TaskModel).all()


def create_task(session: Session, task: TaskCreate) -> TaskModel:
    task = TaskModel(**task.dict())
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def update_task(session: Session, task: TaskUpdate, original: TaskModel) -> TaskModel:
    original.title = task.title
    session.add(original)
    session.commit()
    session.refresh(original)
    return original


def delete_task(session: Session, original: TaskModel):
    session.delete(original)
    session.commit()
