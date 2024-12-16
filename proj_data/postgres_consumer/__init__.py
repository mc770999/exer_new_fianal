from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import os
from dotenv import load_dotenv

Base = declarative_base()

