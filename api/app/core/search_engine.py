from elasticsearch_dsl.connections import connections
from opensearchpy import OpenSearch

# TODO: Config
host = "search-engine"
port = 9200
auth = ("admin", "admin")  # For testing only. Don't store credentials in code.


def set_up():
    client = OpenSearch(
        hosts=[{"host": host, "port": port}],
        http_compress=True,  # enables gzip compression for request bodies
        http_auth=auth,
        use_ssl=False,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
    )

    # Define a default client
    connections.add_connection(alias="default", conn=client)
