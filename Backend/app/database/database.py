import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from sqlalchemy import text


load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")

engine=create_engine(DATABASE_URL)

Base=declarative_base()

SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()







# with engine.connect() as connection:
#     result= connection.execute(text("Select 1"))
#     print(result.fetchone())