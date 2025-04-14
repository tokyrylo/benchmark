from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException

from src.services import BenchmarkService
from src.api.schema import BenchmarkingResponse

from src.api.dependency import get_benchmark_service

router = APIRouter()


@router.get("/results/average", response_model=BenchmarkingResponse)
async def get_average_results(service: BenchmarkService = Depends(get_benchmark_service)):
    """
    Get the average statistics for all stored benchmarking results.

    **Returns:**
     -  `dict`: A dictionary containing keys for **average token count**, **average time to first token**, 
            **average time per output token** and **average total generation time**.
    """
    return await service.get_average_statistics()

@router.get(
        "/results/average/{start_time}/{end_time}", 
        response_model=BenchmarkingResponse,
        responses={
        400: {
            "description": "Invalid date format or date range.",
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid date format. Expected ISO 8601."}
                }
            },
        },
        422: {
            "description": "Validation Error (Path Parameters)",
        },
    }
)
async def get_average_results_between(
    start_time: str,
    end_time: str,
    service: BenchmarkService = Depends(get_benchmark_service),
):
    """
    Get the average statistics for all stored benchmarking results between the given start and end times.

    **Path Parameters:**
     -  `start_time` (str): The start time in ISO 8601 format.
     -  `end_time` (str): The end time in ISO 8601 format.

    **Returns:**
     -  `dict`: A dictionary containing keys for **average token count**, **average time to first token**, 
            **average time per output token** and **average total generation time**.
    """
    try:
        return await service.get_average_statistics_between(start_time, end_time)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))