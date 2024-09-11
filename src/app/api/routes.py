from fastapi import FastAPI, APIRouter

from app.api.news.hundler import (
    get as get_all_news,
    post as create_new_news,
)
from app.api.news.shemas import CreateNewsResponse


def setup_routes(app: FastAPI) -> None:
    api_router = APIRouter(
        prefix='/news',
        tags=['News'],
    )

    api_router.api_route(path='/', methods=['GET'])(get_all_news)
    api_router.api_route(path='/create/', methods=['POST'], response_model=CreateNewsResponse)(create_new_news)

    app.include_router(api_router)
