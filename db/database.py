import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import Session, declarative_base, relationship
from sqlalchemy.dialects.mysql import TIME

load_dotenv()
postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_db = os.getenv("POSTGRES_DB")
postgres_host = os.getenv("POSTGRES_HOST")

engine = create_engine(
    f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}/{postgres_db}"
)

Base = declarative_base()


class Director(Base):
    __tablename__ = "director"
    id = Column(Integer, primary_key=True, nullable=False)
    fio = Column(String(100), nullable=False)


class Movie(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)

    director_id = Column(Integer, ForeignKey("director.id"), nullable=False)

    length = Column(String(8), nullable=False)
    rating = Column(Integer, nullable=False)

    director = relationship("Director")
