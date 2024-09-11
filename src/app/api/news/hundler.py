from fastapi import Depends

from app.api.news.shemas import CreateNewsResponse, ContentCreateRequest
from app.services.contens_crud import OperationService


def get(request: ContentCreateRequest) -> CreateNewsResponse:
    return CreateNewsResponse(
        answer='Done!'
    )


def post(
    request: ContentCreateRequest,
    service: OperationService = Depends()
) -> CreateNewsResponse:
    return service.create(creation_data=request)


def put() -> ...:
    ...


def delete() -> ...:
    ...
