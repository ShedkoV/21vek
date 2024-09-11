from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


engine = create_async_engine(
    url='postgresql+asyncpg://shedko:postgres@localhost:5432/vek_news',
    echo=True,

)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Возвращает асинхронный генератор сессий.

    Используется в FastAPI, где посредством инъекций зависимостей `DI`
    позволяет захватывать соединение с БД соответствующим слоям логики.
    """
    async with async_session() as session:
        yield session
