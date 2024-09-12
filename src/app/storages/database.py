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
    """Getting a session to connect to the database."""
    async with async_session() as session:
        yield session
