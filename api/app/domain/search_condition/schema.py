from app.domain.book.schema import BookSearch
from pydantic import BaseModel, Field


class SearchConditionBase(BaseModel):
    condition: BookSearch = Field(title="検索条件")


class CreateSearchCondition(SearchConditionBase):
    pass


class SearchConditionRead(SearchConditionBase):
    id: int = Field(title="検索条件ID")


class SearchConditionResponse(BaseModel):
    conditions: list[SearchConditionRead]
