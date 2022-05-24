from fastapi import FastAPI

from app.core import search_engine
from app.domain.book import routes as book_router

# Opensearch Client setup
search_engine.set_up()


app = FastAPI()


app.include_router(book_router.router, prefix="/api")
