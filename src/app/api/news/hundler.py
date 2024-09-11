from app.api.news.shemas import CreateNewsRequest, CreateNewsResponse


def get(request: CreateNewsRequest) -> CreateNewsResponse:
    return CreateNewsResponse(
        answer='Done!'
    )


def post(request: CreateNewsRequest) -> CreateNewsResponse:
    answer = request.name
    return CreateNewsResponse(
        id=222,
        name=answer,
        description=answer,
    )


def put() -> ...:
    ...


def delete() -> ...:
    ...
