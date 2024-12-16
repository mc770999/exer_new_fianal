
from sqlalchemy import Column, Integer, ForeignKey, Float
from proj_data.postgres_consumer import Base
from sqlalchemy.orm import relationship

class StudentLifeStyle(Base):
    __tablename__ = 'student_life_style'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    study_hours_per_day = Column(Float, nullable=False)
    extracurricular_hours_per_day = Column(Float, nullable=False)
    sleep_hours_per_day = Column(Float, nullable=False)
    social_hours_per_day = Column(Float, nullable=False)
    physical_activity_hours_per_day = Column(Float, nullable=False)
    gpa = Column(Float, nullable=False)
    stress_level = Column(Integer, nullable=False)

    student = relationship("Student", back_populates="study_data")
