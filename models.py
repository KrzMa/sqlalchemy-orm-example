import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from session import engine

Base = declarative_base(bind=engine)


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    login = Column(String(50), unique=True, nullable=False)
    salary = Column(Float, default=0)
    email = Column(String(50), unique=True, nullable=False)
    registration_date = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f"Author({self.login})"


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    publication_date = Column(DateTime, default=datetime.datetime.now)

    author_id = Column(Integer, ForeignKey("authors.id"))

    def __repr__(self):
        return f"Article({self.title})"


Base.metadata.create_all(engine)
