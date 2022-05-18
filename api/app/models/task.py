from uuid import uuid4

from app.core.database import Base
from sqlalchemy import Column, String


def get_uuid():
    return str(uuid4())


class TaskModel(Base):

    __tablename__ = "tasks"

    id = Column(String(32), primary_key=True, default=get_uuid)
    title = Column(String)
