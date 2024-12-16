from sqlalchemy import Column, Integer, ForeignKey, Float, String, DateTime
from proj_data.postgres_consumer import Base
from sqlalchemy.orm import relationship

class StudentReview(Base):
    __tablename__ = 'student_reviews'

    review_id = Column(String, primary_key=True)
    content = Column(String, nullable=False)
    score = Column(Integer, nullable=False)
    thumbs_up_count = Column(Integer, nullable=False)
    review_created_version = Column(String, nullable=False)
    date_time = Column(DateTime, nullable=False)
    app_version = Column(String, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)

    student = relationship("Student", back_populates="reviews")