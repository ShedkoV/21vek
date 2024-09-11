from pydantic import BaseModel
from datetime import date


class BaseContent(BaseModel):
    """..."""
    name: str
    description: str
    date: date


class ContentCreate(BaseContent):
    """..."""


class Content(BaseContent):
    """..."""
    id: int

    class Config:
        """orm mode on"""
        orm_mode = True
