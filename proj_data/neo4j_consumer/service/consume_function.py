from proj_data.neo4j_consumer.repository.neo4j_repository import create_nodes


def insert_to_neo4j(key, values):
    create_nodes(values)