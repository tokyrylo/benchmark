from fastapi import FastAPI

from src.api.v1.router import router as benchmark_router

app = FastAPI()

app.include_router(benchmark_router)
