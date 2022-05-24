from elasticsearch_dsl import Document
from pydantic import BaseModel


class SearchQuery(BaseModel):
    property: str
    operator: str
    value: str | object

    def to_query_dict(self):
        return dict([(self.property, self.value)])


def search(document: Document, queries: list[SearchQuery]):
    #
    s = document.search()

    for q in queries:
        match q.operator:
            case "EQ":
                s = s.filter("term", **q.to_query_dict())

            case "RANGE":
                s = s.filter("range", **q.to_query_dict())

    return s.execute()
