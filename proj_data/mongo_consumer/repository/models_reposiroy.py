from proj_data.mongo_consumer.database import db


def insert_meny(collection_name,data):
    try:
        collection = db[collection_name]
        result = collection.insert_many(data)
        return result
    except Exception as e:
        print(e)
        return
