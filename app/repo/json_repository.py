from typing import List
from datetime import datetime

from app.config import Config
from app.schema.benchmark import Benchmark
from app.utils.file_utils import read_json_file
from app.repo.benchmark_repo import BenchmarkRepository


class JsonBenchmarkRepository(BenchmarkRepository):
    def __init__(self):
        config = Config()
        if not config.SUPERBENCHMARK_DEBUG:
            raise Exception("The feature is not ready for live yet.")

    async def get_all_results(self) -> List[Benchmark]:
        data = await read_json_file(Config().JSON_DB_PATH)
        return [Benchmark(**item) for item in data["benchmarking_results"]]

    async def get_average_statistics_between(self, start_time: str, end_time: str):
        data = await read_json_file(Config().JSON_DB_PATH)
        start = datetime.fromisoformat(start_time)
        end = datetime.fromisoformat(end_time)
        return [
            Benchmark(**item)
            for item in data["benchmarking_results"]
            if start <= datetime.fromisoformat(item["timestamp"]) <= end
        ]
