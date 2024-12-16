import json

import pandas as pd
from flask import Flask

app = Flask(__name__)

from proj_data.kafka_produser.produser import produce

def split_into_chunks(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


if __name__ == '__main__':
    faust_topic = 'student_teacher_data'

    df_student_profile = pd.read_csv("../data/students-profiles.csv")

    # Convert DataFrame rows to a list of dictionaries
    records_student_profile = df_student_profile.to_dict(orient='records')

    for record in split_into_chunks(records_student_profile, 100):
        produce(faust_topic, "student_profile", record)

    df_student_profile = pd.read_csv("../data/student_lifestyle.csv")

    # Convert DataFrame rows to a list of dictionaries
    records_student_profile = df_student_profile.to_dict(orient='records')

    for record in split_into_chunks(records_student_profile,100):
        produce(faust_topic, "student_lifestyle", record)

    df_student_profile = pd.read_csv("../data/student_course_performance.csv")

    # Convert DataFrame rows to a list of dictionaries
    records_student_profile = df_student_profile.to_dict(orient='records')

    for record in split_into_chunks(records_student_profile, 100):
        produce(faust_topic, "student_course_performance", record)

    df_student_profile = pd.read_csv("../data/reviews_with_students.csv")

    # Convert DataFrame rows to a list of dictionaries
    records_student_profile = df_student_profile.to_dict(orient='records')

    for record in split_into_chunks(records_student_profile, 100):
        produce(faust_topic, "reviews_with_students", record)

    teachers = json.load(open("../data/academic_network.json")).get("teachers")

    for record in split_into_chunks(teachers, 100):
        produce(faust_topic, "teachers", record)

    classes = json.load(open("../data/academic_network.json")).get("classes")

    for record in split_into_chunks(classes, 100):
        produce(faust_topic, "classes", record)

    relationships = json.load(open("../data/academic_network.json")).get("relationships")

    for record in split_into_chunks(relationships, 100):
        produce(faust_topic, "relationships", record)

    app.run()