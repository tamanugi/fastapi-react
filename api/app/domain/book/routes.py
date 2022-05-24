from app.core.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .schema import BookRead, BookSearchResponse

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/search", response_model=BookSearchResponse)
def search_books(session: Session = Depends(get_db)):
    pass
