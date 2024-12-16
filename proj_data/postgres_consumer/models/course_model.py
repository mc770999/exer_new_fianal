from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'  # Name of the table

    id = Column(String, primary_key=True)  # Unique course ID
    course_name = Column(String, nullable=False)  # Course name
    section = Column(Integer, nullable=False)  # Section number
    department = Column(String, nullable=False)  # Department offering the course
    semester = Column(String, nullable=False)  # Semester the course is offered
    room = Column(String, nullable=False)  # Room where the course is conducted
    schedule = Column(String, nullable=False)  # Schedule (e.g., Tue 11:00)
    teacher_id = Column(String, ForeignKey('professors.id'), nullable=False)