import pytest
from app.domain.book import service
from app.domain.book.model import BookModel
from app.domain.book.schema import BookSearch
from elasticsearch_dsl.connections import connections
from opensearchpy import OpenSearch


@pytest.fixture(scope="module", autouse=True)
def setup():
    client = OpenSearch(
        # TODO: from config
        hosts=[{"host": "search-engine", "port": 9200}],
        http_compress=True,  # enables gzip compression for request bodies
        use_ssl=False,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
    )
    # Define a default Elasticsearch client
    connections.add_connection(alias="default", conn=client)
    BookModel.init()


def test_book_search():
    BookModel(meta={"_id": 1}, isbn="test1", title="title1", price=99).save()
    BookModel(meta={"_id": 2}, isbn="test2", title="title2", price=100).save()
    BookModel(meta={"_id": 3}, isbn="test3", title="title3", price=101).save()

    bs = BookSearch(keyword="hoge")
    res = service.search(bs)
    assert len(res.hits) == 0

    bs = BookSearch(keyword="test")
    res = service.search(bs)
    assert len(res.hits) == 3

    bs = BookSearch(keyword="test1")
    res = service.search(bs)
    assert len(res.hits) == 1
