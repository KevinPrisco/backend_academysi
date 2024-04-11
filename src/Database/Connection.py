from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "mysql://root:@localhost/AcademySIBD"
# "BDtype://user:password@dblocation/Dbname"

db_engine = create_engine(SQLALCHEMY_DATABASE_URL)

Sessionlocal = sessionmaker (bind=db_engine)

Base = declarative_base()
