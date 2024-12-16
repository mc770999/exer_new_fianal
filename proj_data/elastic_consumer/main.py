import os
from dotenv import load_dotenv
from proj_data.kafka_consume.kafka_consumer import consume_topic

load_dotenv(verbose=True)

if __name__ == '__main__':
    try:
        topic_name = os.environ['ELASTIC_SEARCH_TOPIC']
        consume_topic(topic_name)
    except KeyboardInterrupt:
        pass
