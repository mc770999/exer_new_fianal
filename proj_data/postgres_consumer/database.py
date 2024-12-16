from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import os
from dotenv import load_dotenv
from proj_data.postgres_consumer import Base

load_dotenv(verbose=True)

engine = create_engine(os.environ['DATABASE_POSTGRES_URL'])

session_maker = sessionmaker(bind=engine)


def sead():
    Base.metadata.create_all(engine)
