from pydantic import BaseModel, Field


class BookRead(BaseModel):
    isbn: str = Field(title="ISBN", example="978-4-910519-03-6")
    title: str = Field(title="タイトル", example="踊るハシビロコウ")
    sub_title: str = Field(title="サブタイトル", example="衝撃の巨鳥こんな姿、見たことない!!")
    author: str = Field(title="著者", example="南幅俊輔 著")
    publisher: str = Field(title="出版社", example="ライブ・パブリッシング")
    published_at: str = Field(title="出版年月", example="2022.5")
    series: str = Field(title="シリーズ", example="")
    price: str = Field(title="本体価格", example="¥1300")

class BookSearchResponse(BaseModel):
    books: list[BookRead]
    count: int
