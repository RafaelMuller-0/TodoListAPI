from sqlalchemy import create_engine
from sqlalchemy import URL
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from os import getenv
from dotenv import load_dotenv

load_dotenv()

database = URL.create(
    "postgresql+psycopg",
    host=getenv("DATABASE_HOST"),
    port=int(getenv("DATABASE_PORT","5432")),
    database=getenv("DATABASE_NAME"),
    username=getenv("DATABASE_USER"),
    password=getenv("DATABASE_PASSWORD")
)
engine = create_engine(database)
SessionDB = sessionmaker(engine)

def get_connection():
    con = engine.connect()
    try:
        yield con
    finally:
        con.close()

def get_session():
    with SessionDB() as session:
        yield session