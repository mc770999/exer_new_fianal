import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv(verbose=True)

neo4j_uri = os.environ.get("NEO4J_URI")
user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(
    uri=neo4j_uri,
    auth=(user,password)
)