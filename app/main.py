from fastapi import FastAPI
from . import api

app = FastAPI(title="GeoIP API Service")

app.include_router(api.router)
