import pytest
from datetime import datetime

from unittest.mock import patch, AsyncMock

from src.repo.json_repository import JsonBenchmarkRepository

# Моковані дані
mock_data = {
    "benchmarking_results": [
        {
            "request_id": "1",
            "prompt_text": "Test Prompt 1",
            "generated_text": "Test Output 1",
            "token_count": 5,
            "time_to_first_token": 150,
            "time_per_output_token": 30,
            "total_generation_time": 300,
            "timestamp": "2024-06-01T12:00:00",
        },
        {
            "request_id": "2",
            "prompt_text": "Test Prompt 2",
            "generated_text": "Test Output 2",
            "token_count": 10,
            "time_to_first_token": 100,
            "time_per_output_token": 20,
            "total_generation_time": 200,
            "timestamp": "2024-06-02T12:00:00",
        },
    ]
}


@pytest.fixture
def benchmark_repo():
    with patch("app.config.Config") as mock_config:
        mock_config().SUPERBENCHMARK_DEBUG = True
        repo = JsonBenchmarkRepository()
        yield repo


@pytest.mark.asyncio
@patch("app.utils.file_utils.read_json_file", new_callable=AsyncMock)
async def test_get_all_results(mock_read_json_file, benchmark_repo):
    mock_read_json_file.return_value = mock_data
    results = await benchmark_repo.get_all_results()

    assert len(results) > 0
    assert all("request_id" in result.dict() for result in results)


@pytest.mark.asyncio
@patch("app.utils.file_utils.read_json_file", new_callable=AsyncMock)
async def test_get_average_statistics_between(mock_read_json_file, benchmark_repo):
    mock_read_json_file.return_value = mock_data

    start_time = "2024-06-01T00:00:00"
    end_time = "2024-06-02T23:59:59"
    results = await benchmark_repo.get_average_statistics_between(start_time, end_time)

    assert len(results) > 0
    assert all(
        start_time <= result.timestamp.isoformat() <= end_time for result in results
    )
