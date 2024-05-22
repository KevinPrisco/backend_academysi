# from sqlalchemy import create_engine, URL
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from config import DB_DRIVER, DB_USER, \
# DB_HOST, DB_NAME
# # DB_PASSWORD, DB_PORT, 

# SQLALCHEMY_DATABASE_URL = URL.create( 
#     drivername=DB_DRIVER,
#     username=DB_USER,
#     # password=DB_PASSWORD,
#     # port= DB_PORT,
#     host=DB_HOST,
#     database=DB_NAME
#  )


# db_engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessionlocal = sessionmaker(bind=db_engine)

# Base = declarative_base()


# def get_db():
#     db = Sessionlocal()
#     try:
#         yield db
#     finally:
#         db.close()
