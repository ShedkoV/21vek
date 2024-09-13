from typing import Any

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeMeta

Base: DeclarativeMeta = declarative_base()


class Content(Base):  # type: ignore[valid-type, misc]
    """Table views in database."""

    __tablename__ = 'contents'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def as_dict(self) -> dict[str, Column[Any]]:  # noqa: D102
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }
