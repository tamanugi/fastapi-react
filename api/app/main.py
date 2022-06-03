from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import search_engine
from app.domain.book import routes as book_router
from app.domain.search_condition import routes as search_condition_router

# Opensearch Client setup
search_engine.set_up()

app = FastAPI()

origins = [
    # TODO: use config
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(book_router.router, prefix="/api")
app.include_router(search_condition_router.router, prefix="/api")
