import logging

from fastapi import Depends, HTTPException, Response, status
from fastapi_cache.decorator import cache

from app.api.contents.schemas import ContentCreateRequest, ContentResponse, ContentUpdate
from app.services.contents_crud import OperationService

service_dependency = Depends(OperationService)


@cache(expire=60)
async def get_all_content(
    service: OperationService = service_dependency,
) -> list[ContentResponse]:
    """Get all content records."""
    return await service.get_list_contents()


@cache(expire=60)
async def get_content_by_id(
    content_id: int,
    service: OperationService = service_dependency,
) -> ContentResponse:
    """Get content record by id."""
    response = await service.get_item(content_id=content_id)
    if not response:
        logging.info(f'No record in the database with id={content_id}')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return response


async def create(
    request: ContentCreateRequest,
    service: OperationService = service_dependency,
) -> ContentResponse:
    """Create new record."""
    return await service.create(creation_data=request)


async def update(
    content_id: int,
    request: ContentUpdate,
    service: OperationService = service_dependency,
) -> ContentResponse:
    """Update record by id."""
    updated_result = service.update(content_id=content_id, request=request)
    if not updated_result:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return await updated_result


async def delete(
    content_id: int,
    service: OperationService = service_dependency,
) -> Response:
    """Delete record by id."""
    if not await service.delete(content_id=content_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
