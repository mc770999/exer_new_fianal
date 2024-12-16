# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import declarative_base, sessionmaker
#
# engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/test1")
# session_maker = sessionmaker(bind=engine)
#
# Base = declarative_base()
#
# class User(Base):
#     __tablename__ =  "enosh"
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     name = Column(String)
#
#
# Base.metadata.create_all(engine)