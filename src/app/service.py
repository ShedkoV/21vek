import logging

from fastapi import FastAPI

from app.api.routes import setup_routes

app = FastAPI()
logging.basicConfig(level=logging.INFO)
setup_routes(app)
