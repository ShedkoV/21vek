from fastapi import Depends

from app.api.news.shemas import ContentCreateRequest, ContentUpdate
from app.decorators.log_result import log_result
from app.storages.database import Session, get_session
from app.storages.tables import Contents as table_operation


class OperationService:
    """Operation Service"""

    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def _get(self, content_id: int) -> table_operation:
        """get operation by id"""
        return self.session.query(table_operation).filter_by(id=content_id).first()

    @log_result
    def get_list_contents(self) -> list[table_operation]:
        """..."""
        query = self.session.query(table_operation)
        return query.all()

    @log_result
    def get_item(self, content_id: int) -> table_operation:
        """Get operation"""
        return self._get(content_id)

    @log_result
    def create(self, creation_data: ContentCreateRequest) -> table_operation:
        """Creation operation"""
        operation = table_operation(**creation_data.dict())
        self.session.add(operation)
        self.session.commit()

        return operation

    @log_result
    def update(self, content_id: int, request: ContentUpdate) -> table_operation:
        """"""
        operation = self._get(content_id)
        if operation:
            for field, value in request:
                setattr(operation, field, value)
            self.session.commit()

        return operation

    @log_result
    def delete(self, content_id: int) -> table_operation:
        """Delete operation"""
        operation = self._get(content_id)
        if operation:
            self.session.delete(operation)
            self.session.commit()
            operation = True

        return operation
