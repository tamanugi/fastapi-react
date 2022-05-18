from app.models.task import TaskModel
from sqlalchemy.orm import Session


def fetch_tasks(session: Session) -> list[TaskModel]:
    return session.query(TaskModel).all()


def create_task():
    pass


def update_task():
    pass
