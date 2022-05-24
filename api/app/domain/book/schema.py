from app.domain.book.model import BookModel
from pydantic import BaseModel, Field


class BookSearch(BaseModel):
    keyword: str | None
    published_at_ge: str | None
    published_at_le: str | None
    price_ge: int | None
    price_le: int | None


class BookRead(BaseModel):
    isbn: str = Field(title="ISBN", example="978-4-910519-03-6")
    title: str = Field(title="タイトル", example="踊るハシビロコウ")
    sub_title: str = Field(title="サブタイトル", example="衝撃の巨鳥こんな姿、見たことない!!", default="")
    author: str = Field(title="著者", example="南幅俊輔 著", default="")
    publisher: str = Field(title="出版社", example="ライブ・パブリッシング", default="")
    published_at: str = Field(title="出版年月", example="2022.5", default="")
    series: str = Field(title="シリーズ", example="", default="")
    price: int = Field(title="本体価格", example=1300, default=0)

    @staticmethod
    def from_model(model: BookModel):
        return BookRead(**model.to_dict())


class BookSearchResponse(BaseModel):
    books: list[BookRead]
    count: int
