from pydantic import BaseModel


class TaskRead(BaseModel):
    id: str
    title: str


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(TaskCreate):
    pass
