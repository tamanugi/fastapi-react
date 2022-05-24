from elasticsearch_dsl import Document, Integer, Text


class BookModel(Document):
    isbn: str = Text()
    title: str = Text()
    sub_title: str = Text()
    author: str = Text()
    publisher: str = Text()
    published_at: str = Text()
    series: str = Text()
    price: str = Integer()

    class Index:
        name = "books"
