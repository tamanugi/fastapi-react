from typing import Any

from app.domain.book.model import BookModel
from app.domain.book.schema import BookAggregation, BookSearch
from elasticsearch_dsl import A, Q

unlimited_size = 3000


def __keyword_target_fileds() -> list[str]:
    return ["isbn", "title", "sub_title", "author", "publisher", "series"]


def __create_dict_without_none(**kwargs: Any) -> dict:
    return {k: v for k, v in kwargs.items() if v is not None}


def search(bs: BookSearch) -> Any:
    s = BookModel.search()

    for query in book_search_to_queries(bs):
        s = s.query(query)

    # TODO: paginate
    s = s[0:unlimited_size]

    return s.execute()


def book_search_to_queries(bs: BookSearch) -> list[Q]:
    queries = []

    if bs.keyword is not None:
        q = Q(
            "multi_match",
            query=f"{bs.keyword}",
            fields=__keyword_target_fileds(),
        )
        queries.append(q)

    if bs.publisher is not None:
        q = Q("term", publisher__keyword=bs.publisher)
        queries.append(q)

    if bs.price_ge is not None or bs.price_le is not None:
        range_dict = __create_dict_without_none(gte=bs.price_ge, lte=bs.price_le)
        q = Q("range", price=range_dict)
        queries.append(q)

    return queries


def aggs(field_name: str) -> list[BookAggregation]:
    s = BookModel.search()

    a = A("terms", field=f"{field_name}.keyword", size=unlimited_size)

    aggs_name = f"{field_name}_aggs"

    s = s.source(False)
    s.aggs.bucket(aggs_name, a)

    response = s.execute()
    return [
        BookAggregation(**agg.to_dict())
        for agg in response.aggregations[aggs_name]["buckets"]
    ]
