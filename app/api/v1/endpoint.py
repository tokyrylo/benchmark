from fastapi import APIRouter, Depends

from app.repo.json_repository import JsonBenchmarkRepository
from app.services.benchmark_service import BenchmarkService

router = APIRouter()


def get_benchmark_service():
    repository = JsonBenchmarkRepository()
    return BenchmarkService(repository)


@router.get("/results/average")
async def get_average_results(
    service: BenchmarkService = Depends(get_benchmark_service),
):
    return await service.get_average_statistics()


@router.get("/results/average/{start_time}/{end_time}")
async def get_average_results_between(
    start_time: str,
    end_time: str,
    service: BenchmarkService = Depends(get_benchmark_service),
):
    return await service.get_average_statistics_between(start_time, end_time)
