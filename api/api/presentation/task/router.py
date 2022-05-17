from api.presentation.task.schema import TaskCreate, TaskResponse, TaskUpdate
from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=list[TaskResponse])
def list_tasks():
    pass


@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    pass


@router.patch("/{id}", response_model=TaskResponse)
def update_task(id: str, task: TaskUpdate):
    pass


@router.delete("/{id}")
def delete_task(id: str):
    pass
