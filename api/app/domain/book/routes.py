from fastapi import APIRouter, Depends

from . import service as book_search_service
from .schema import (
    BookConditionPublisherResponse,
    BookRead,
    BookSearch,
    BookSearchResponse,
)

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/search", response_model=BookSearchResponse)
def search_books(query: BookSearch = Depends()):
    response = book_search_service.search(query)
    books = [BookRead.from_model(book_model) for book_model in response]
    return BookSearchResponse(books=books, count=len(books))


@router.get(
    "/search/conditions/publisher", response_model=BookConditionPublisherResponse
)
def search_conditions_publisher():
    aggs = book_search_service.aggs("publisher")

    print(aggs)
    return BookConditionPublisherResponse(candidates=aggs)
