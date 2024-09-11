import logging

from fastapi import Depends, HTTPException, status, Response

from app.api.news.shemas import ContentCreateRequest, ContentResponse, ContentUpdate
from app.services.contents_crud import OperationService


def get_all_content(
    service: OperationService = Depends(),
) -> list[ContentResponse]:
    return service.get_list_contents()


def get_content_by_id(
    content_id: int,
    service: OperationService = Depends(),
) -> ContentResponse:
    response = service.get_item(content_id=content_id)
    if not response:
        logging.info(f'No record in the database with id={content_id}')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return response


def create(
    request: ContentCreateRequest,
    service: OperationService = Depends()
) -> ContentResponse:
    return service.create(creation_data=request)


def update(
    content_id: int,
    request: ContentUpdate,
    service: OperationService = Depends(),
) -> ContentResponse:
    updated_result = service.update(content_id=content_id, request=request)
    if not updated_result:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return updated_result


def delete(
    content_id: int,
    service: OperationService = Depends(),
) -> Response:
    if not service.delete(content_id=content_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
