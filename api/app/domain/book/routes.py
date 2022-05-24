from fastapi import APIRouter, Depends

from . import service as book_search_service
from .schema import BookRead, BookSearch, BookSearchResponse

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/search", response_model=BookSearchResponse)
def search_books(query: BookSearch = Depends()):
    response = book_search_service.search(query)
    books = [BookRead.from_model(book_model) for book_model in response]
    return BookSearchResponse(books=books, count=len(books))
