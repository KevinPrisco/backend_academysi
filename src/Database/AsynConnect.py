from sqlalchemy import  URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ..config import DB_DRIVER, DB_USER, DB_PASSWORD, DB_PORT, DB_HOST, DB_NAME


SQLALCHEMY_DATABASE_URL = URL.create( 
    drivername=DB_DRIVER,
    username=DB_USER,
    password=DB_PASSWORD,
    port= DB_PORT,
    host=DB_HOST,
    database=DB_NAME
 )



db_engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
Sessionlocal = async_sessionmaker(bind=db_engine, class_=AsyncSession)
Base = declarative_base()

async def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        await db.close()

