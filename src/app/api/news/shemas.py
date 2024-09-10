from pydantic import BaseModel, Field


class BaseNews(BaseModel):
    """..."""
    name: str = Field(
        ...,
        description='Название загаловка',
        example='Срочные новости',
    )
    description: str = Field(
        ...,
        description='Контент новостей',
        example='Очень интересные новости',
    )


class CreateNewsRequest(BaseNews):
    """..."""


class CreateNewsResponse(BaseNews):
    """..."""
    id: int = Field(
        ...,
        description='Уникальный номер',
        example='3fa85f64-5717-4562-b3fc-2c963f66afa6',
    )
