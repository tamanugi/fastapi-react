from api.usecase.task.task_command_model import TaskCreate, TaskUpdate
from api.usecase.task.task_command_usecase import TaskCommandUsecase
from api.usecase.task.task_query_model import TaskRead
from api.usecase.task.task_query_usecase import TaskQueryUsecase
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/tasks", tags=["tasks"])


def _task_query_usecase() -> TaskQueryUsecase:
    return TaskQueryUsecase()


def _task_command_usecase() -> TaskCommandUsecase:
    return TaskCommandUsecase()


@router.get("/", response_model=list[TaskRead])
def list_tasks(task_query_usecase: TaskQueryUsecase = Depends(_task_query_usecase)):
    return task_query_usecase.fetch_tasks()


@router.post("/", response_model=TaskRead)
def create_task(
    task: TaskCreate,
    task_command_usecase: TaskCommandUsecase = Depends(_task_command_usecase),
):
    pass


@router.patch("/{id}", response_model=TaskRead)
def update_task(
    id: str,
    task: TaskUpdate,
    task_command_usecase: TaskCommandUsecase = Depends(_task_command_usecase),
):
    pass


@router.delete("/{id}")
def delete_task(
    id: str,
    task_command_usecase: TaskCommandUsecase = Depends(_task_command_usecase),
):
    pass
