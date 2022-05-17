from pydantic import BaseModel, Field


class TaskRead(BaseModel):
    id: str = Field(example="idhogehoge")
    title: str = Field(example="buy milk")
