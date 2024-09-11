from fastapi import Depends

from app.api.news.shemas import ContentCreateRequest, ContentUpdate
from app.utils.decorators.log_result import log_result
from app.storages.database import async_session, get_session
from app.storages.tables import Contents as table_operation
from sqlalchemy import select


class OperationService:
    """Operation Service"""

    def __init__(self, session: async_session = Depends(get_session)) -> None:
        self.session = session

    async def _get(self, content_id: int) -> table_operation:
        """Получение операции по ID"""
        async with self.session.begin():
            result = await self.session.execute(select(table_operation).where(table_operation.id == content_id))
            return result.scalar_one_or_none()

    @log_result
    async def get_list_contents(self) -> list[table_operation]:
        """..."""
        async with self.session.begin():
            result = await self.session.execute(select(table_operation))
            return result.scalars().all()

    @log_result
    async def get_item(self, content_id: int) -> table_operation:
        """Get operation"""
        return await self._get(content_id)

    @log_result
    async def create(self, creation_data: ContentCreateRequest) -> table_operation:
        """Создание операции"""
        async with self.session.begin():
            operation = table_operation(**creation_data.dict())
            self.session.add(operation)
            await self.session.commit()

            return operation

    async def update(self, content_id: int, request: ContentUpdate) -> table_operation:
        """Обновление операции"""
        operation = await self._get(content_id)
        if operation:
            for field, value in request.dict().items():
                setattr(operation, field, value)
            await self.session.commit()
            await self.session.refresh(operation)
        return operation

    @log_result
    async def delete(self, content_id: int) -> table_operation:
        """Удаление операции"""
        operation = await self._get(content_id)
        if operation:
            await self.session.delete(operation)
            await self.session.commit()
            operation = True
        return operation
