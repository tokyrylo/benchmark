from fastapi import FastAPI

from app.api.v1 import endpoint
from app.config import Config

app = FastAPI()

config = Config()
if config.SUPERBENCHMARK_DEBUG:
    print("DEBUG mode is enabled")
else:
    print("DEBUG mode is disabled")

app.include_router(endpoint.router)
