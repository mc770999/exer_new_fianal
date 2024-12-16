import pandas as pd


def convert_csv_to_json(student_profile,student_life_style="", student_course="", student_review=""):
    # Read CSV into a pandas DataFrame
    df_student_profile = pd.read_csv(student_profile)

    # Convert DataFrame rows to a list of dictionaries
    records_student_profile = df_student_profile.to_dict(orient='records')

    # Process each record to ensure correct serialization
    students : {} = convert_to_dict(records_student_profile)

    df_life_style = pd.read_csv(student_life_style)

    add_to_students(students, df_life_style, "life_style")

    df_student_course = pd.read_csv(student_course)

    add_to_students(students, df_student_course, "student_course")

    df_student_reviews = pd.read_csv(student_review)

    add_to_students(students, df_student_reviews, "student_reviews")

    return students




def add_to_students(students, df, type):
    # Group the DataFrame by the 'id' column
    student_id = 'Student_ID' if 'Student_ID' in df else "student_id" if "student_id" in df else False
    print(student_id)
    if not student_id:
        return None
    grouped = df.groupby(student_id)

    # Convert each group into a list of dictionaries
    grouped_records = {}
    for group_id, group_data in grouped:
        # Convert group data to a list of dictionaries
        students[group_id][type] = group_data.to_dict(orient='records')






def convert_to_dict(records):
    data = {}
    for record in records:
        data[record["id"]] = record
    return data



