from flask import Flask
from kafka import KafkaProducer
import os
import json

app = Flask(__name__)

from dotenv import load_dotenv
load_dotenv(verbose=True)


def produce(topic, key, message):
    kafka_producer = KafkaProducer(
        bootstrap_servers = os.environ['BOOTSTRAP_SERVERS'],
        value_serializer= lambda v: json.dumps(v).encode('utf-8')
    )
    kafka_producer.send(
        topic,
        value=message,
        key=key.encode('utf-8')
    )
    kafka_producer.flush()



