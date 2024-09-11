from fastapi import Depends

from app.models.content import ContentCreate
from app.storages.database import Session, get_session
from app.storages.tables import Contents as table_operation


class OperationService:
    """Operation Service"""
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def create(self, creation_data: ContentCreate) -> table_operation:
        """Creation operation"""
        operation = table_operation(
            **creation_data.dict(),
        )
        self.session.add(operation)
        self.session.commit()

        return operation
