import os
from dotenv import load_dotenv
from proj_data.kafka_consume.kafka_consumer import consume_topic
from proj_data.neo4j_consumer.service.consume_function import insert_to_neo4j

load_dotenv(verbose=True)

if __name__ == '__main__':
    try:
        topic_name = os.environ['NEO4J_TOPIC']
        consume_topic(topic_name, insert_to_neo4j)
    except KeyboardInterrupt:
        pass
