from app.domain.book.model import BookModel
from app.domain.book.schema import BookSearch
from elasticsearch_dsl import Q


def __keyword_target_fileds():
    return ["isbn", "title", "sub_title", "author", "publisher"]


def __create_dict_without_none(**kwargs):
    return {k: v for k, v in kwargs.items() if v is not None}


def search(bs: BookSearch):
    s = BookModel.search()

    for query in book_search_to_queries(bs):
        s = s.query(query)

    return s.execute()


def book_search_to_queries(bs: BookSearch):
    queries = []

    if bs.keyword is not None:
        q = Q(
            "query_string",
            query=f"*{bs.keyword}*",
            fields=__keyword_target_fileds(),
        )
        queries.append(q)

    if bs.published_at_ge is not None or bs.published_at_le is not None:
        range_dict = __create_dict_without_none(
            gte=bs.published_at_ge, lte=bs.published_at_le
        )
        q = Q("range", published_at=range_dict)
        queries.append(q)

    if bs.price_ge is not None or bs.price_le is not None:
        range_dict = __create_dict_without_none(gte=bs.price_ge, lte=bs.price_le)
        q = Q("range", price=range_dict)
        queries.append(q)

    return queries
