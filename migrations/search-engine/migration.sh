#!/bin/sh

INDEX_NAME=books

EXEC_CMD="docker compose exec search-engine"

# delete index
$EXEC_CMD curl --user admin:admin -X DELETE --insecure "https://localhost:9200/$INDEX_NAME?pretty"

# create index
$EXEC_CMD curl --user admin:admin -X PUT -H "Content-Type: application/json" --insecure  "https://localhost:9200/$INDEX_NAME?pretty" -d'
{
    "settings":{
        "analysis":{
            "tokenizer" : {
                "kuromoji" : {
                   "type" : "kuromoji_tokenizer"
                }
            },
            "analyzer": {
                "default": {
                    "type": "custom",
                    "tokenizer": "kuromoji"
                }
            }
        }
    }
}'

# bulk dataset
cat dataset.json | jq -c '.[] | ({"index":{"_index": "books", "_id": .isbn}}, .)' > tmp_dataset.json
docker compose cp tmp_dataset.json search-engine:/tmp/tmp_dataset.json 
$EXEC_CMD curl --user admin:admin -X PUT --insecure "https://localhost:9200/$INDEX_NAME/_bulk?pretty&refresh"  -H "Content-Type: application/json" --data-binary "@/tmp/tmp_dataset.json"

rm tmp_dataset.json
 