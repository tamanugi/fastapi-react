from fastapi import FastAPI

from app.core.database import engine
from app.models import task as task_model
from app.routes import task as task_router

# TODO: migraton library
task_model.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(task_router.router, prefix="/api")
