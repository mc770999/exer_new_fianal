import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# Load environment variables from .env file
load_dotenv(verbose=True)

# Get environment variables
es_host = os.getenv("ES_HOST", "localhost")
es_port = os.getenv("ES_PORT", "9200")
es_username = os.getenv("ES_USERNAME", "elastic")
es_password = os.getenv("ES_PASSWORD", "1234")




# Create the Elasticsearch client
es_client = Elasticsearch(
    f"http://{es_host}:{es_port}",
    basic_auth=(es_username, es_password),
    verify_certs=False
)
print(es_client)


# Example: Create an index and add a document
index_name = "test-index"
documents = [{
    "title": "Elasticsearch Test2",
    "content": "This is a test document"
}]


# Index a document
bulk(client=es_client, body=documents)

# Search the document
response = es_client.search(index=index_name, body={
    "query": {
        "match": {
            "title": "test2"
        }
    }
})
print(response)
