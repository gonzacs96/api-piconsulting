from os import environ
from src.entities.base_entity import Base
from sqlalchemy import create_engine as sql_alchemy_create_engine
from sqlalchemy.orm import sessionmaker, Session


def create_engine():
    return sql_alchemy_create_engine(
        environ["DB_CONNECTION_STRING"], echo=environ["DB_ECHO"] == "True"
    )


def test_db_connection_and_create_tables():
    try:
        engine = create_engine()
        Base.metadata.create_all(engine)
    except Exception as error:
        print(f"Error connecting to database: {error}")
        raise error


def get_db():
    try:
        engine = create_engine()
        session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db: Session = session()
        yield db
    finally:
        db.close()
