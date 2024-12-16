
from sqlalchemy import Column, Integer, ForeignKey, String, Float
from proj_data.postgres_consumer import Base
from sqlalchemy.orm import relationship


class StudentCoursePerformance(Base):
    __tablename__ = 'student_course_performance'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_name = Column(String, primary_key=True)
    current_grade = Column(Float, nullable=False)
    attendance_rate = Column(Float, nullable=False)
    assignments_completed = Column(Integer, nullable=False)
    missed_deadlines = Column(Integer, nullable=False)
    participation_score = Column(Float, nullable=False)
    midterm_grade = Column(Float, nullable=False)
    study_group_attendance = Column(Integer, nullable=False)
    office_hours_visits = Column(Integer, nullable=False)
    extra_credit_completed = Column(Integer, nullable=False)
