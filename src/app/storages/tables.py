from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Content(Base):
    """Table views in database."""

    __tablename__ = 'contents'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def as_dict(self):  # noqa: D102
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }
