from proj_data.postgres_consumer.models.course_model import Course
from proj_data.postgres_consumer.models.student_course_performance import StudentCoursePerformance
from proj_data.postgres_consumer.models.student_model import Student
from proj_data.postgres_consumer.models.student_review import StudentReview
from proj_data.postgres_consumer.models.student_study_data import StudentLifeStyle
from proj_data.postgres_consumer.models.teacher import Teacher
from proj_data.postgres_consumer.repository.models_repository import insert_models_to_db


def insert_from_kafka_to_postgres(key, values):
    key = key.decode("utf-8")
    match key:
        case "student_profile":
            try:
                insert_models_to_db(Student, values)
            except Exception as e:
                print(e)
                return
        case "student_lifestyle":
            try:
                insert_models_to_db(StudentLifeStyle, values)
            except Exception as e:
                print(e)
                return
        case "student_course_performance":
            try:
                insert_models_to_db(StudentCoursePerformance, values)
            except Exception as e:
                print(e)
                return
        case "reviews_with_students":
            try:
                insert_models_to_db(StudentReview, values)
            except Exception as e:
                print(e)
                return
        case "teachers":
            try:
                insert_models_to_db(Teacher, values)
            except Exception as e:
                print(e)
                return
        case "classes":
            try:
                insert_models_to_db(Course, values)
            except Exception as e:
                print(e)
                return




""" reviews_with_students
    student_course_performance
    student_lifestyle
    student_profile"""