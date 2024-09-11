from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contents(Base):
    """...."""
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
