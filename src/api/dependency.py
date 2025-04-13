from src.config import settings
from src.services import BenchmarkService
from src.infrastructure import JSONBenchmarkRepository


def get_benchmark_service() -> BenchmarkService:
    repo = JSONBenchmarkRepository(file_path=settings.JSON_DB_PATH)
    return BenchmarkService(repo)