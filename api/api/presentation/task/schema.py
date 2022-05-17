from pydantic import BaseModel, Field


class TaskResponse(BaseModel):
    id: str = Field(example="idhogehoge")
    title: str = Field(example="buy milk")


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(TaskCreate):
    pass
