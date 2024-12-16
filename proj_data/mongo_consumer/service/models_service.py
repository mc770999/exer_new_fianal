from proj_data.mongo_consumer.repository.models_reposiroy import insert_meny


def insert_from_kafka_to_mongo(key, value):
    try:
        res = insert_meny(key, value)
        return res
    except Exception as e:
        print(e)
        return