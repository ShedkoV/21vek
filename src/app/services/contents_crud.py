import logging
from typing import Optional, Union

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.api.contents.schemas import ContentRequest
from app.storages.database import async_session, get_session
from app.storages.tables import Content as table_operation  # noqa: N813
from app.utils.decorators.log_result import log_result

default_session = Depends(get_session)


class OperationService:
    """Operation Service."""

    def __init__(self, session: async_session = default_session) -> None:
        self.session = session

    @log_result
    async def get_list_contents(self) -> list[table_operation]:
        """Get all contents."""
        async with self.session.begin():
            result = await self.session.execute(select(table_operation))
            return result.scalars().all()

    @log_result
    async def get_item(self, content_id: int) -> Optional[table_operation]:
        """Get content."""
        return await self._get(content_id)

    @log_result
    async def create(self, creation_data: ContentRequest) -> table_operation:
        """Creating content."""
        async with self.session.begin():
            operation = table_operation(**creation_data.dict())
            self.session.add(operation)
            await self.session.commit()

            return operation

    @log_result
    async def update(self, content_id: int, request: ContentRequest) -> Optional[table_operation]:
        """Updating content."""
        operation = await self._get(content_id)
        if operation:
            for field, value in request.dict().items():
                setattr(operation, field, value)
            await self.session.commit()
            await self.session.refresh(operation)
        return operation

    @log_result
    async def delete(self, content_id: int) -> Optional[table_operation]:
        """Deleted content."""
        operation = await self._get(content_id)
        if operation:
            await self.session.delete(operation)
            await self.session.commit()
            return operation

    async def _get(self, content_id: int) -> Optional[table_operation]:
        """Get content by id."""
        try:
            async with self.session.begin():
                result = await self.session.execute(
                    select(table_operation).where(table_operation.id == content_id),
                )
                return result.scalar_one_or_none()
        except (OSError, SQLAlchemyError) as error_msg:
            logging.info(f'Error with Database: {error_msg}')
