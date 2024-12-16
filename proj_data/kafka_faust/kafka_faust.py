import os
from dotenv import load_dotenv
import faust
# Load environment variables
load_dotenv(verbose=True)


# Faust app for stream processing
app = faust.App(
    'streaming',  # App name
    broker=os.environ['BOOTSTRAP_SERVERS'],  # Kafka broker
    value_serializer='json'  # Message value format
)
student_teacher_data_topic = app.topic(os.environ['STUDENT_TEACHER_DATA_TOPIC'])


# Define a Kafka topic to consume from
elastic_search_topic = app.topic(os.environ['ELASTIC_SEARCH_TOPIC'])
mongo_db_topic = app.topic(os.environ['MONGO_TOPIC'])
neo4j_topic = app.topic(os.environ['NEO4J_TOPIC'])
postgres_sql_topic = app.topic(os.environ['POSTGRES_SQL_TOPIC'])




# Stream processing agent
@app.agent(student_teacher_data_topic)
async def process_person(stream):
    async for event in stream.events():
        # Perform some processing
        print(event.key.decode('utf-8'), event.value)
        await mongo_db_topic.send(key=event.key,value=event.value)

        if event.key.decode('utf-8') != "relationships":
            await postgres_sql_topic.send(key=event.key,value=event.value)


        if event.key.decode('utf-8') == "relationships":
            await neo4j_topic.send(key=event.key,value=event.value)


        if event.key.decode('utf-8') == "reviews_with_students":
            await elastic_search_topic.send(key=event.key,value=event.value)


        print(f"Processed and sent: key: {event.key.decode('utf-8')}, value: {event.value}")



if __name__ == '__main__':
    # Run Faust in one thread
    app.main()