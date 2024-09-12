from typing import Optional

from pydantic import BaseModel, Field


class BaseContent(BaseModel):
    """Base content."""

    name: Optional[str] = Field(
        description='Название загаловка',
        example='Срочные новости',
    )
    description: Optional[str] = Field(
        description='Контент новостей',
        example='Очень интересные новости',
    )


class ContentRequest(BaseContent):
    """Content request."""


class ContentResponse(BaseContent):
    """Content response."""

    id: int = Field(
        description='Уникальный номер',
        example='3fa85f64-5717-4562-b3fc-2c963f66afa6',
    )

    class Config:  # pylint: disable=too-few-public-methods
        """Orm mode on."""

        from_attributes = True
