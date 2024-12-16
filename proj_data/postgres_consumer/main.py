import os
from dotenv import load_dotenv
from proj_data.kafka_consume.kafka_consumer import consume_topic
from proj_data.postgres_consumer.database import sead
from proj_data.postgres_consumer.service.insert_to_sql import insert_from_kafka_to_postgres

load_dotenv(verbose=True)

if __name__ == '__main__':
    sead()
    try:
        topic_name = os.environ["POSTGRES_SQL_TOPIC"]
        print(topic_name)
        consume_topic(topic_name, insert_from_kafka_to_postgres)
    except Exception as e:
        print(e)
        pass
