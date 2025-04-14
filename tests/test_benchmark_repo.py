import unittest
from datetime import datetime
from typing import AsyncGenerator

from src.infrastructure.repository import JSONBenchmarkRepository
from src.domain.entities import BenchmarkingResult


def fake_read_benchmarking_results(_: str) -> AsyncGenerator[BenchmarkingResult, None]:
    """
    Фейковый генератор вместо read_benchmarking_results — возвращает 2 объекта.
    """
    results = [
        BenchmarkingResult(
            request_id="1",
            timestamp=datetime.fromisoformat("2025-04-13T10:00:00"),
            token_count=100,
            time_to_first_token=0.2,
            time_per_output_token=0.04,
            total_generation_time=5.0,
            prompt_text="Hello",
            generated_text="Hi"
        ),
        BenchmarkingResult(
            request_id="2",
            timestamp=datetime.fromisoformat("2025-04-13T11:00:00"),
            token_count=200,
            time_to_first_token=0.3,
            time_per_output_token=0.05,
            total_generation_time=8.0,
            prompt_text="How are you?",
            generated_text="I'm good"
        )
    ]

    async def _gen():
        for r in results:
            yield r

    return _gen()


class TestJSONBenchmarkRepository(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        import src.infrastructure.repository.json_benchmark_repository as repo_module
        repo_module.read_benchmarking_results = fake_read_benchmarking_results
        self.repo = JSONBenchmarkRepository(file_path="fake_path.json")

    async def test_all_returns_all_results(self):
        results = await self.repo.all()
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].request_id, "1")
        self.assertEqual(results[1].token_count, 200)

    async def test_get_by_request_id_success(self):
        result = await self.repo.get(reference="1")
        self.assertIsNotNone(result)
        self.assertEqual(result.request_id, "1")

    async def test_get_by_request_id_not_found(self):
        result = await self.repo.get(reference="999")
        self.assertIsNone(result)

    async def test_add_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            await self.repo.add(BenchmarkingResult(
                request_id="3",
                timestamp=datetime.now(),
                token_count=123,
                time_to_first_token=0.1,
                time_per_output_token=0.03,
                total_generation_time=6.0,
                prompt_text="Test prompt",
                generated_text="Test output"
            ))

    async def test_update_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            await self.repo.update(BenchmarkingResult(
                request_id="3",
                timestamp=datetime.now(),
                token_count=123,
                time_to_first_token=0.1,
                time_per_output_token=0.03,
                total_generation_time=6.0,
                prompt_text="Test prompt",
                generated_text="Test output"
            ))

    async def test_delete_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            await self.repo.delete(BenchmarkingResult(
                request_id="3",
                timestamp=datetime.now(),
                token_count=123,
                time_to_first_token=0.1,
                time_per_output_token=0.03,
                total_generation_time=6.0,
                prompt_text="Test prompt",
                generated_text="Test output"
            ))


if __name__ == "__main__":
    unittest.main()
