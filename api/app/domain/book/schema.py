from app.domain.book.model import BookModel
from pydantic import BaseModel, Field


class BookSearch(BaseModel):
    keyword: str | None
    price_ge: int | None
    price_le: int | None
    publisher: str | None
    limit: int = 10
    page: int = 1


class BookRead(BaseModel):
    isbn: str = Field(title="ISBN", example="978-4-910519-03-6")
    title: str = Field(title="タイトル", example="踊るハシビロコウ")
    sub_title: str = Field(title="サブタイトル", example="衝撃の巨鳥こんな姿、見たことない!!", default="")
    author: str = Field(title="著者", example="南幅俊輔 著", default="")
    publisher: str = Field(title="出版社", example="ライブ・パブリッシング", default="")
    published_at: str = Field(title="出版年月", example="2022.5", default="")
    series: str = Field(title="シリーズ", example="", default="")
    price: int = Field(title="本体価格", example=1300, default=0)

    @classmethod
    def from_model(cls, model: BookModel) -> "BookRead":
        return cls(**model.to_dict())


class BookSearchResponse(BaseModel):
    books: list[BookRead]
    count: int


class BookAggregation(BaseModel):
    key: str
    doc_count: int


class BookConditionPublisherResponse(BaseModel):
    candidates: list[BookAggregation]
