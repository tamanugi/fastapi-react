from fastapi import FastAPI

from app.core.database import engine
from app.domain.book import routes as book_router


app = FastAPI()


app.include_router(book_router.router, prefix="/api")
