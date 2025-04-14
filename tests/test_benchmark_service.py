import unittest
from datetime import datetime

from src.services.benchmark_service import BenchmarkService
from src.domain.entities import BenchmarkingResult


class MockRepository:
    def __init__(self, data):
        self._data = data

    async def all(self):
        return self._data


class TestBenchmarkService(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.mock_data = [
            BenchmarkingResult(
                request_id="1",
                timestamp=datetime.fromisoformat("2025-04-13T10:00:00"),
                token_count=100,
                time_to_first_token=0.2,
                time_per_output_token=0.04,
                total_generation_time=5.0,
                prompt_text="Some prompt",
                generated_text="Some output"
            ),
            BenchmarkingResult(
                request_id="2",
                timestamp=datetime.fromisoformat("2025-04-13T11:00:00"),
                token_count=200,
                time_to_first_token=0.3,
                time_per_output_token=0.05,
                total_generation_time=8.0,
                prompt_text="Another prompt",
                generated_text="Another output",
            ),
        ]

    async def test_get_average_statistics(self):
        service = BenchmarkService(MockRepository(self.mock_data))
        result = await service.get_average_statistics()

        self.assertEqual(result["avg_token_count"], 150)
        self.assertAlmostEqual(result["avg_time_to_first_token"], 0.25, places=2)
        self.assertAlmostEqual(result["avg_time_per_output_token"], 0.045, places=3)
        self.assertEqual(result["avg_total_generation_time"], 6.5)

    async def test_get_average_statistics_empty(self):
        service = BenchmarkService(MockRepository([]))
        result = await service.get_average_statistics()
        self.assertEqual(result, {})

    async def test_get_average_statistics_between(self):
        service = BenchmarkService(MockRepository(self.mock_data))

        start = "2025-04-13T10:30:00"
        end = "2025-04-13T11:30:00"

        result = await service.get_average_statistics_between(start, end)

        self.assertEqual(result["avg_token_count"], 200)
        self.assertEqual(result["avg_total_generation_time"], 8.0)

    async def test_get_average_statistics_between_empty(self):
        service = BenchmarkService(MockRepository(self.mock_data))

        start = "2025-04-13T12:00:00"
        end = "2025-04-13T13:00:00"

        result = await service.get_average_statistics_between(start, end)
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()
