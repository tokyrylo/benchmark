from datetime import datetime
import pytest

from unittest.mock import AsyncMock

from app.shema.benchmark import Benchmark
from app.services.benchmark_service import BenchmarkService


@pytest.fixture
def benchmark_service():
    mock_repo = AsyncMock()
    return BenchmarkService(mock_repo)


@pytest.mark.asyncio
async def test_calculate_average_statistic(benchmark_service):
    mock_results = [
        Benchmark(
            request_id="1",
            prompt_text="Test Prompt 1",
            generated_text="Test Output 1",
            token_count=5,
            time_to_first_token=150,
            time_per_output_token=30,
            total_generation_time=300,
            timestamp=datetime.now(),
        ),
        Benchmark(
            request_id="2",
            prompt_text="Test Prompt 2",
            generated_text="Test Output 2",
            token_count=6,
            time_to_first_token=200,
            time_per_output_token=25,
            total_generation_time=350,
            timestamp=datetime.now(),
        ),
    ]

    avg_stats = await benchmark_service.calculate_average_statistic(mock_results)
    assert avg_stats["avarage_token_count"] == 5.5
    assert avg_stats["avarage_time_to_first_token"] == 175
    assert avg_stats["avarage_time_per_token_output"] == 27.5
    assert avg_stats["avarage_total_generation_time"] == 325


@pytest.mark.asyncio
async def test_get_average_statistics(benchmark_service):
    benchmark_service.repository.get_all_results = AsyncMock(
        return_value=[
            Benchmark(
                request_id="1",
                prompt_text="Test Prompt 1",
                generated_text="Test Output 1",
                token_count=5,
                time_to_first_token=150,
                time_per_output_token=30,
                total_generation_time=300,
                timestamp=datetime.now(),
            )
        ]
    )
    avg_stats = await benchmark_service.get_average_statistics()
    assert avg_stats["avarage_token_count"] == 5
