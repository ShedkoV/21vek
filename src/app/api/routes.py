from fastapi import APIRouter, FastAPI

from app.api.contents.handler import create, delete, get_all_content, get_content_by_id, update
from app.api.contents.schemas import ContentResponse


def setup_routes(app: FastAPI) -> None:
    """Setting up routers."""
    api_router = APIRouter(prefix='/content', tags=['Content'])

    api_router.api_route(
        path='/',
        methods=['GET'],
        response_model=list[ContentResponse],
    )(get_all_content)

    api_router.api_route(
        path='/{content_id}',
        methods=['GET'],
        response_model=ContentResponse,
    )(get_content_by_id)

    api_router.api_route(
        path='/create/',
        methods=['POST'],
        response_model=ContentResponse,
    )(create)

    api_router.api_route(
        path='/{content_id}',
        methods=['PUT'],
        response_model=ContentResponse,
    )(update)

    api_router.api_route(
        path='/{content_id}',
        methods=['DELETE'],
        response_model=ContentResponse,
    )(delete)

    app.include_router(api_router)
