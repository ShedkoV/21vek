import logging

from fastapi import FastAPI

from app.api.routes import setup_routes
from app.utils.cache.cache import lifespan


app = FastAPI(lifespan=lifespan)
logging.basicConfig(level=logging.INFO)
setup_routes(app)
