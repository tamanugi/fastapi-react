#!/bin/sh

INDEX_NAME=books

EXEC_CMD="docker compose exec search-engine"

# delete index
$EXEC_CMD curl -X DELETE "localhost:9200/$INDEX_NAME?pretty"

# create index
$EXEC_CMD curl -X PUT "localhost:9200/$INDEX_NAME?pretty"

# bulk dataset
cat dataset.json | jq -c '.[] | ({"index":{"_index": "books", "_id": .isbn}}, .)' > tmp_dataset.json
docker compose cp tmp_dataset.json search-engine:/tmp/tmp_dataset.json 
$EXEC_CMD curl -X PUT "http://localhost:9200/$INDEX_NAME/_bulk?pretty&refresh"  -H "Content-Type: application/json" --data-binary "@/tmp/tmp_dataset.json"

rm tmp_dataset.json
 