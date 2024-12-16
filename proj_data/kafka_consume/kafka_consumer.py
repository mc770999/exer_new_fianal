import json
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer

load_dotenv(verbose=True)



def consume_topic(topic_name, function):
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='earliest',  # Read messages from the beginning
        group_id=f"{topic_name}_group",  # Group ID for the consumer group
    )

    print(f"Listening to topic: {topic_name}")

    # Continuously listen for messages
    for message in consumer:
        key = message.key.decode('utf-8') if message.key else None
        function(key, message.value)
        print(f"Topic: {topic_name}, Key: {key}, Value: {message.value}")





