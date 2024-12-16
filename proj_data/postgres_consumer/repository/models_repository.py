from proj_data.postgres_consumer.database import session_maker


def insert_models_to_db(model,json_list):
    with session_maker() as session:
        session.bulk_insert_mappings(model, json_list)
        session.commit()