from sqlalchemy import Column, Integer, String

from db import Base


class StudentSQL(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)