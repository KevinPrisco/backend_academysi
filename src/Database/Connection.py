from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DB_CONNECT

SQLALCHEMY_DATABASE_URL = DB_CONNECT

db_engine = create_engine(SQLALCHEMY_DATABASE_URL)

Sessionlocal = sessionmaker (bind=db_engine)

Base = declarative_base()

