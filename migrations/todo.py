from sqlalchemy import Column, Integer, String
from migrations.main import Base

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    job = Column(String(256))