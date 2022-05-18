from pydantic import BaseModel


class TaskRead(BaseModel):
    id: str
    title: str

    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(TaskCreate):
    pass
