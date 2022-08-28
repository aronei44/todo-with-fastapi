from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///todo.db")
engine = create_engine("postgresql://postgres:admin123@localhost:5432/todo")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)