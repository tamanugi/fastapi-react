from app.core.database import Base
from sqlalchemy import Column, String


class TaskModel(Base):

    __tablename__ = "tasks"

    id = Column(String(32), primary_key=True)
    title = Column(String)
